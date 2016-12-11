Notes On Subject Terms
======================

In our current setup (Providence 1.4 as of 2016-12-11), Subject Terms are not vocabulary lists, but metadata elements (element_id=177) associated with objects (table_num=57[1]). 

They are text metadata elements and their relationships to objects are stored in the database table `ca_attributes`. The labels (actual strings for the subject terms e.g. "Anti-globalization", "Anarchism", "Feminism") are related in `ca_attribute_values`.

For more information on metadata elements and attributes [go here](http://docs.collectiveaccess.org/wiki/API:Metadata_Elements_and_Attributes)

With the results from a query like:

    select count(distint(attribute_id)) from ca_attribute_values where element_id = 177 and value_longtext1 like 'Anarchism';

There are **61** total, unique attribute records with the same value, leading us to believe that this piece of data, as it is configured, is not normalized.[2] This would probably account for the reason why there is no straighforward front-end configuration to allow for clicking on subject terms and getting a list of other related objects. 

### Stats

Of 2240 subject terms entered across all objects as of 2016-12-11, there are 857 unique subject terms in use.[3] 
 


Used this query to dump information about all subject terms and the objects they are related to:

    select cav.*, ca.*, ol.name from ca_attribute_values cav left join ca_attributes ca on (cav.attribute_id=ca.attribute_id) left join ca_object_labels ol on (ol.object_id=ca.row_id) where ca.element_id = 177;

See [subject_terms_2016_12_11.csv]() (needs to be cleaned up)


### Notes to the notes

[1] For more information on the data model, you can refer to `datamodel.conf` in Providence.
[2] This is also true if we examine the uniqueness of the `value_id` field for the table. 
[3] Though this is before any much needed string reconcilliation, so this number might actually be lower (e.g., we would consider the string 'Anti-globalization' and 'Anti-globablization   ' to be the same, but with the extra whitespace, they are probably considered different strings iby the database). We should be able to clean some of this up in the database with:
    
    UPDATE `ca_attribute_values` SET `value_longtext1` = LOWER(TRIM(`value_longtext1`));







