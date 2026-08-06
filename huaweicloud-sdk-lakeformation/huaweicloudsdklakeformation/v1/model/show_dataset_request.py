# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatasetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'catalog_name': 'str',
        'dataset_name': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'dataset_name': 'dataset_name',
        'database_name': 'database_name'
    }

    def __init__(self, instance_id=None, catalog_name=None, dataset_name=None, database_name=None):
        r"""ShowDatasetRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释:** LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** 不涉及
        :type instance_id: str
        :param catalog_name: **参数解释:** catalog名称。 **约束限制:** 只能包含字母、数字和下划线，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及
        :type catalog_name: str
        :param dataset_name: **参数解释:** 数据集名称。 **约束限制:** 只能包含中文、字母、数字和_-特殊字符，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及 
        :type dataset_name: str
        :param database_name: **参数解释:** 数据库名称。 **约束限制:** 只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。 **取值范围:** 长度为1~128个字符 **默认取值:** 不涉及 
        :type database_name: str
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._dataset_name = None
        self._database_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.dataset_name = dataset_name
        self.database_name = database_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDatasetRequest.

        **参数解释:** LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** 不涉及

        :return: The instance_id of this ShowDatasetRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDatasetRequest.

        **参数解释:** LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** 不涉及

        :param instance_id: The instance_id of this ShowDatasetRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ShowDatasetRequest.

        **参数解释:** catalog名称。 **约束限制:** 只能包含字母、数字和下划线，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及

        :return: The catalog_name of this ShowDatasetRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ShowDatasetRequest.

        **参数解释:** catalog名称。 **约束限制:** 只能包含字母、数字和下划线，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及

        :param catalog_name: The catalog_name of this ShowDatasetRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this ShowDatasetRequest.

        **参数解释:** 数据集名称。 **约束限制:** 只能包含中文、字母、数字和_-特殊字符，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及 

        :return: The dataset_name of this ShowDatasetRequest.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this ShowDatasetRequest.

        **参数解释:** 数据集名称。 **约束限制:** 只能包含中文、字母、数字和_-特殊字符，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及 

        :param dataset_name: The dataset_name of this ShowDatasetRequest.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowDatasetRequest.

        **参数解释:** 数据库名称。 **约束限制:** 只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。 **取值范围:** 长度为1~128个字符 **默认取值:** 不涉及 

        :return: The database_name of this ShowDatasetRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowDatasetRequest.

        **参数解释:** 数据库名称。 **约束限制:** 只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。 **取值范围:** 长度为1~128个字符 **默认取值:** 不涉及 

        :param database_name: The database_name of this ShowDatasetRequest.
        :type database_name: str
        """
        self._database_name = database_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDatasetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
