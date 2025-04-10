# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'sorted': 'str',
        'name': 'str',
        'app': 'str',
        'ief_instance_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sorted': 'sorted',
        'name': 'name',
        'app': 'app',
        'ief_instance_id': 'ief-instance-id'
    }

    def __init__(self, limit=None, offset=None, sorted=None, name=None, app=None, ief_instance_id=None):
        r"""ListServicesRequest

        The model defined in huaweicloud sdk

        :param limit: 指定分页查询每页的行数，最大为100，默认值为10。
        :type limit: int
        :param offset: 指定要查询的偏移数量，默认为0。
        :type offset: int
        :param sorted: 响应中查询到的服务将按照指定的字段进行排序
        :type sorted: str
        :param name: 服务名称
        :type name: str
        :param app: 按照相关的应用查询服务
        :type app: str
        :param ief_instance_id: 铂金版实例ID
        :type ief_instance_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._sorted = None
        self._name = None
        self._app = None
        self._ief_instance_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sorted is not None:
            self.sorted = sorted
        if name is not None:
            self.name = name
        if app is not None:
            self.app = app
        self.ief_instance_id = ief_instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListServicesRequest.

        指定分页查询每页的行数，最大为100，默认值为10。

        :return: The limit of this ListServicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServicesRequest.

        指定分页查询每页的行数，最大为100，默认值为10。

        :param limit: The limit of this ListServicesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListServicesRequest.

        指定要查询的偏移数量，默认为0。

        :return: The offset of this ListServicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListServicesRequest.

        指定要查询的偏移数量，默认为0。

        :param offset: The offset of this ListServicesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sorted(self):
        r"""Gets the sorted of this ListServicesRequest.

        响应中查询到的服务将按照指定的字段进行排序

        :return: The sorted of this ListServicesRequest.
        :rtype: str
        """
        return self._sorted

    @sorted.setter
    def sorted(self, sorted):
        r"""Sets the sorted of this ListServicesRequest.

        响应中查询到的服务将按照指定的字段进行排序

        :param sorted: The sorted of this ListServicesRequest.
        :type sorted: str
        """
        self._sorted = sorted

    @property
    def name(self):
        r"""Gets the name of this ListServicesRequest.

        服务名称

        :return: The name of this ListServicesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListServicesRequest.

        服务名称

        :param name: The name of this ListServicesRequest.
        :type name: str
        """
        self._name = name

    @property
    def app(self):
        r"""Gets the app of this ListServicesRequest.

        按照相关的应用查询服务

        :return: The app of this ListServicesRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ListServicesRequest.

        按照相关的应用查询服务

        :param app: The app of this ListServicesRequest.
        :type app: str
        """
        self._app = app

    @property
    def ief_instance_id(self):
        r"""Gets the ief_instance_id of this ListServicesRequest.

        铂金版实例ID

        :return: The ief_instance_id of this ListServicesRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        r"""Sets the ief_instance_id of this ListServicesRequest.

        铂金版实例ID

        :param ief_instance_id: The ief_instance_id of this ListServicesRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

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
        if not isinstance(other, ListServicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
