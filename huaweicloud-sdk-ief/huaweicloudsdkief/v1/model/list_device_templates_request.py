# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeviceTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'name': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, ief_instance_id=None, name=None, offset=None, limit=None):
        r"""ListDeviceTemplatesRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param name: 终端设备名称，模糊匹配
        :type name: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: str
        :param limit: 每页显示的条目数量，取值范围1~1000，默认为1000
        :type limit: str
        """
        
        

        self._ief_instance_id = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def ief_instance_id(self):
        r"""Gets the ief_instance_id of this ListDeviceTemplatesRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListDeviceTemplatesRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        r"""Sets the ief_instance_id of this ListDeviceTemplatesRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListDeviceTemplatesRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def name(self):
        r"""Gets the name of this ListDeviceTemplatesRequest.

        终端设备名称，模糊匹配

        :return: The name of this ListDeviceTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDeviceTemplatesRequest.

        终端设备名称，模糊匹配

        :param name: The name of this ListDeviceTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListDeviceTemplatesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListDeviceTemplatesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDeviceTemplatesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListDeviceTemplatesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDeviceTemplatesRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :return: The limit of this ListDeviceTemplatesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDeviceTemplatesRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :param limit: The limit of this ListDeviceTemplatesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListDeviceTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
