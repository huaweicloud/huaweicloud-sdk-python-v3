# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceParamResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'updated': 'str',
        'configuration_parameter': 'list[ConfigurationParameterList]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'updated': 'updated',
        'configuration_parameter': 'configuration_parameter',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, id=None, name=None, description=None, updated=None, configuration_parameter=None, offset=None, limit=None, total=None):
        r"""ShowInstanceParamResponse

        The model defined in huaweicloud sdk

        :param id: 参数组id。
        :type id: str
        :param name: 参数组名称。
        :type name: str
        :param description: 参数组描述。
        :type description: str
        :param updated: DDM参数最后更新时间。
        :type updated: str
        :param configuration_parameter: DDM实例参数信息列表的集合。
        :type configuration_parameter: list[:class:`huaweicloudsdkddm.v1.ConfigurationParameterList`]
        :param offset: 分页参数: 起始值。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        :param total: 集合总数
        :type total: int
        """
        
        super(ShowInstanceParamResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._updated = None
        self._configuration_parameter = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if updated is not None:
            self.updated = updated
        if configuration_parameter is not None:
            self.configuration_parameter = configuration_parameter
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceParamResponse.

        参数组id。

        :return: The id of this ShowInstanceParamResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceParamResponse.

        参数组id。

        :param id: The id of this ShowInstanceParamResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceParamResponse.

        参数组名称。

        :return: The name of this ShowInstanceParamResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceParamResponse.

        参数组名称。

        :param name: The name of this ShowInstanceParamResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowInstanceParamResponse.

        参数组描述。

        :return: The description of this ShowInstanceParamResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowInstanceParamResponse.

        参数组描述。

        :param description: The description of this ShowInstanceParamResponse.
        :type description: str
        """
        self._description = description

    @property
    def updated(self):
        r"""Gets the updated of this ShowInstanceParamResponse.

        DDM参数最后更新时间。

        :return: The updated of this ShowInstanceParamResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowInstanceParamResponse.

        DDM参数最后更新时间。

        :param updated: The updated of this ShowInstanceParamResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def configuration_parameter(self):
        r"""Gets the configuration_parameter of this ShowInstanceParamResponse.

        DDM实例参数信息列表的集合。

        :return: The configuration_parameter of this ShowInstanceParamResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ConfigurationParameterList`]
        """
        return self._configuration_parameter

    @configuration_parameter.setter
    def configuration_parameter(self, configuration_parameter):
        r"""Sets the configuration_parameter of this ShowInstanceParamResponse.

        DDM实例参数信息列表的集合。

        :param configuration_parameter: The configuration_parameter of this ShowInstanceParamResponse.
        :type configuration_parameter: list[:class:`huaweicloudsdkddm.v1.ConfigurationParameterList`]
        """
        self._configuration_parameter = configuration_parameter

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceParamResponse.

        分页参数: 起始值。

        :return: The offset of this ShowInstanceParamResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceParamResponse.

        分页参数: 起始值。

        :param offset: The offset of this ShowInstanceParamResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceParamResponse.

        分页参数：每页多少条。

        :return: The limit of this ShowInstanceParamResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceParamResponse.

        分页参数：每页多少条。

        :param limit: The limit of this ShowInstanceParamResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ShowInstanceParamResponse.

        集合总数

        :return: The total of this ShowInstanceParamResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowInstanceParamResponse.

        集合总数

        :param total: The total of this ShowInstanceParamResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowInstanceParamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
