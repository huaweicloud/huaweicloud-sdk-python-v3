# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateZonesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'tags': 'str',
        'name': 'str',
        'status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'tags': 'tags',
        'name': 'name',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, type=None, limit=None, marker=None, offset=None, tags=None, name=None, status=None, enterprise_project_id=None):
        """ListPrivateZonesRequest

        The model defined in huaweicloud sdk

        :param type: 待查询的zone的类型。  取值范围：private。
        :type type: str
        :param limit: 每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时为查询第一页。  默认值为空。
        :type marker: str
        :param offset: 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。
        :type offset: int
        :param tags: 资源标签。
        :type tags: str
        :param name: zone名称。
        :type name: str
        :param status: 资源状态。
        :type status: str
        :param enterprise_project_id: 域名关联的企业项目ID，长度不超过36个字符。  默认值为0。
        :type enterprise_project_id: str
        """
        
        

        self._type = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._tags = None
        self._name = None
        self._status = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.type = type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this ListPrivateZonesRequest.

        待查询的zone的类型。  取值范围：private。

        :return: The type of this ListPrivateZonesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPrivateZonesRequest.

        待查询的zone的类型。  取值范围：private。

        :param type: The type of this ListPrivateZonesRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListPrivateZonesRequest.

        每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :return: The limit of this ListPrivateZonesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPrivateZonesRequest.

        每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :param limit: The limit of this ListPrivateZonesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPrivateZonesRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :return: The marker of this ListPrivateZonesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPrivateZonesRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :param marker: The marker of this ListPrivateZonesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListPrivateZonesRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。

        :return: The offset of this ListPrivateZonesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPrivateZonesRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当前设置marker不为空时，以marker为分页起始标识。

        :param offset: The offset of this ListPrivateZonesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this ListPrivateZonesRequest.

        资源标签。

        :return: The tags of this ListPrivateZonesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListPrivateZonesRequest.

        资源标签。

        :param tags: The tags of this ListPrivateZonesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def name(self):
        """Gets the name of this ListPrivateZonesRequest.

        zone名称。

        :return: The name of this ListPrivateZonesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPrivateZonesRequest.

        zone名称。

        :param name: The name of this ListPrivateZonesRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListPrivateZonesRequest.

        资源状态。

        :return: The status of this ListPrivateZonesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPrivateZonesRequest.

        资源状态。

        :param status: The status of this ListPrivateZonesRequest.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPrivateZonesRequest.

        域名关联的企业项目ID，长度不超过36个字符。  默认值为0。

        :return: The enterprise_project_id of this ListPrivateZonesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPrivateZonesRequest.

        域名关联的企业项目ID，长度不超过36个字符。  默认值为0。

        :param enterprise_project_id: The enterprise_project_id of this ListPrivateZonesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListPrivateZonesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
