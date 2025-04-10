# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpaceAnalysisRequest:

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
        'x_language': 'str',
        'object_type': 'str',
        'database_id': 'str',
        'offset': 'str',
        'limit': 'str',
        'show_instance_info': 'str',
        'datastore_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'object_type': 'object_type',
        'database_id': 'database_id',
        'offset': 'offset',
        'limit': 'limit',
        'show_instance_info': 'show_instance_info',
        'datastore_type': 'datastore_type'
    }

    def __init__(self, instance_id=None, x_language=None, object_type=None, database_id=None, offset=None, limit=None, show_instance_info=None, datastore_type=None):
        r"""ListSpaceAnalysisRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param x_language: 语言
        :type x_language: str
        :param object_type: 对象类型
        :type object_type: str
        :param database_id: 数据库ID
        :type database_id: str
        :param offset: 偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。offset必须是limit的整数倍。
        :type offset: str
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: str
        :param show_instance_info: 是否返回实例级别数据，取值：true或者false
        :type show_instance_info: str
        :param datastore_type: 引擎类型
        :type datastore_type: str
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._object_type = None
        self._database_id = None
        self._offset = None
        self._limit = None
        self._show_instance_info = None
        self._datastore_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        self.object_type = object_type
        if database_id is not None:
            self.database_id = database_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if show_instance_info is not None:
            self.show_instance_info = show_instance_info
        self.datastore_type = datastore_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSpaceAnalysisRequest.

        实例ID

        :return: The instance_id of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSpaceAnalysisRequest.

        实例ID

        :param instance_id: The instance_id of this ListSpaceAnalysisRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSpaceAnalysisRequest.

        语言

        :return: The x_language of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSpaceAnalysisRequest.

        语言

        :param x_language: The x_language of this ListSpaceAnalysisRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def object_type(self):
        r"""Gets the object_type of this ListSpaceAnalysisRequest.

        对象类型

        :return: The object_type of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListSpaceAnalysisRequest.

        对象类型

        :param object_type: The object_type of this ListSpaceAnalysisRequest.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def database_id(self):
        r"""Gets the database_id of this ListSpaceAnalysisRequest.

        数据库ID

        :return: The database_id of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        r"""Sets the database_id of this ListSpaceAnalysisRequest.

        数据库ID

        :param database_id: The database_id of this ListSpaceAnalysisRequest.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def offset(self):
        r"""Gets the offset of this ListSpaceAnalysisRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。offset必须是limit的整数倍。

        :return: The offset of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSpaceAnalysisRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。offset必须是limit的整数倍。

        :param offset: The offset of this ListSpaceAnalysisRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSpaceAnalysisRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSpaceAnalysisRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListSpaceAnalysisRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def show_instance_info(self):
        r"""Gets the show_instance_info of this ListSpaceAnalysisRequest.

        是否返回实例级别数据，取值：true或者false

        :return: The show_instance_info of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._show_instance_info

    @show_instance_info.setter
    def show_instance_info(self, show_instance_info):
        r"""Sets the show_instance_info of this ListSpaceAnalysisRequest.

        是否返回实例级别数据，取值：true或者false

        :param show_instance_info: The show_instance_info of this ListSpaceAnalysisRequest.
        :type show_instance_info: str
        """
        self._show_instance_info = show_instance_info

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListSpaceAnalysisRequest.

        引擎类型

        :return: The datastore_type of this ListSpaceAnalysisRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListSpaceAnalysisRequest.

        引擎类型

        :param datastore_type: The datastore_type of this ListSpaceAnalysisRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

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
        if not isinstance(other, ListSpaceAnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
