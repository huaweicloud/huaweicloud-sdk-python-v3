# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatasetsRequest:

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
        'database_name': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool',
        'name_partern': 'str',
        'format': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page',
        'name_partern': 'name_partern',
        'format': 'format'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, limit=None, marker=None, reverse_page=None, name_partern=None, format=None):
        r"""ListDatasetsRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释:** LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** 不涉及
        :type instance_id: str
        :param catalog_name: **参数解释:** catalog名称。 **约束限制:** 只能包含字母、数字和下划线，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及
        :type catalog_name: str
        :param database_name: **参数解释:** 数据库名称。 **约束限制:** 只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。 **取值范围:** 长度为1~128个字符 **默认取值:** 不涉及 
        :type database_name: str
        :param limit: **参数解释:** 查询返回条数。 **约束限制:** 取值为0~1000 **取值范围:** 取值为0~1000 **默认取值:** 1000
        :type limit: int
        :param marker: **参数解释:** 查询的起始记录ID。 **约束限制:** 长度为0~256个字符 **取值范围:** 长度为0~256个字符 **默认取值:** 不涉及
        :type marker: str
        :param reverse_page: **参数解释:** 是否查询上一页。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** false
        :type reverse_page: bool
        :param name_partern: **参数解释:** 数据集名称通配符，用于模糊查询。 **约束限制:** 只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符
        :type name_partern: str
        :param format: 数据格式 描述文件的组织方式：行存储/文本/图片/音频/视频/自定义
        :type format: str
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self._name_partern = None
        self._format = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page
        if name_partern is not None:
            self.name_partern = name_partern
        if format is not None:
            self.format = format

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDatasetsRequest.

        **参数解释:** LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** 不涉及

        :return: The instance_id of this ListDatasetsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDatasetsRequest.

        **参数解释:** LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** 不涉及

        :param instance_id: The instance_id of this ListDatasetsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ListDatasetsRequest.

        **参数解释:** catalog名称。 **约束限制:** 只能包含字母、数字和下划线，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及

        :return: The catalog_name of this ListDatasetsRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ListDatasetsRequest.

        **参数解释:** catalog名称。 **约束限制:** 只能包含字母、数字和下划线，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符 **默认取值:** 不涉及

        :param catalog_name: The catalog_name of this ListDatasetsRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListDatasetsRequest.

        **参数解释:** 数据库名称。 **约束限制:** 只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。 **取值范围:** 长度为1~128个字符 **默认取值:** 不涉及 

        :return: The database_name of this ListDatasetsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListDatasetsRequest.

        **参数解释:** 数据库名称。 **约束限制:** 只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。 **取值范围:** 长度为1~128个字符 **默认取值:** 不涉及 

        :param database_name: The database_name of this ListDatasetsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def limit(self):
        r"""Gets the limit of this ListDatasetsRequest.

        **参数解释:** 查询返回条数。 **约束限制:** 取值为0~1000 **取值范围:** 取值为0~1000 **默认取值:** 1000

        :return: The limit of this ListDatasetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDatasetsRequest.

        **参数解释:** 查询返回条数。 **约束限制:** 取值为0~1000 **取值范围:** 取值为0~1000 **默认取值:** 1000

        :param limit: The limit of this ListDatasetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListDatasetsRequest.

        **参数解释:** 查询的起始记录ID。 **约束限制:** 长度为0~256个字符 **取值范围:** 长度为0~256个字符 **默认取值:** 不涉及

        :return: The marker of this ListDatasetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListDatasetsRequest.

        **参数解释:** 查询的起始记录ID。 **约束限制:** 长度为0~256个字符 **取值范围:** 长度为0~256个字符 **默认取值:** 不涉及

        :param marker: The marker of this ListDatasetsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        r"""Gets the reverse_page of this ListDatasetsRequest.

        **参数解释:** 是否查询上一页。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** false

        :return: The reverse_page of this ListDatasetsRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        r"""Sets the reverse_page of this ListDatasetsRequest.

        **参数解释:** 是否查询上一页。 **约束限制:** 不涉及 **取值范围:** 不涉及 **默认取值:** false

        :param reverse_page: The reverse_page of this ListDatasetsRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

    @property
    def name_partern(self):
        r"""Gets the name_partern of this ListDatasetsRequest.

        **参数解释:** 数据集名称通配符，用于模糊查询。 **约束限制:** 只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符

        :return: The name_partern of this ListDatasetsRequest.
        :rtype: str
        """
        return self._name_partern

    @name_partern.setter
    def name_partern(self, name_partern):
        r"""Sets the name_partern of this ListDatasetsRequest.

        **参数解释:** 数据集名称通配符，用于模糊查询。 **约束限制:** 只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~256个字符。 **取值范围:** 长度为1~256个字符

        :param name_partern: The name_partern of this ListDatasetsRequest.
        :type name_partern: str
        """
        self._name_partern = name_partern

    @property
    def format(self):
        r"""Gets the format of this ListDatasetsRequest.

        数据格式 描述文件的组织方式：行存储/文本/图片/音频/视频/自定义

        :return: The format of this ListDatasetsRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ListDatasetsRequest.

        数据格式 描述文件的组织方式：行存储/文本/图片/音频/视频/自定义

        :param format: The format of this ListDatasetsRequest.
        :type format: str
        """
        self._format = format

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
        if not isinstance(other, ListDatasetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
