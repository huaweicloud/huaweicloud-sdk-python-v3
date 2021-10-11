# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackendInstancesV2Request:


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
        'vpc_channel_id': 'str',
        'name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vpc_channel_id': 'vpc_channel_id',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, vpc_channel_id=None, name=None, limit=None, offset=None):
        """ListBackendInstancesV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._vpc_channel_id = None
        self._name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        self.vpc_channel_id = vpc_channel_id
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBackendInstancesV2Request.

        实例编号

        :return: The instance_id of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBackendInstancesV2Request.

        实例编号

        :param instance_id: The instance_id of this ListBackendInstancesV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def vpc_channel_id(self):
        """Gets the vpc_channel_id of this ListBackendInstancesV2Request.

        VPC通道的编号

        :return: The vpc_channel_id of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        """Sets the vpc_channel_id of this ListBackendInstancesV2Request.

        VPC通道的编号

        :param vpc_channel_id: The vpc_channel_id of this ListBackendInstancesV2Request.
        :type: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def name(self):
        """Gets the name of this ListBackendInstancesV2Request.

        云服务器的名称

        :return: The name of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBackendInstancesV2Request.

        云服务器的名称

        :param name: The name of this ListBackendInstancesV2Request.
        :type: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListBackendInstancesV2Request.

        每页显示的条数

        :return: The limit of this ListBackendInstancesV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackendInstancesV2Request.

        每页显示的条数

        :param limit: The limit of this ListBackendInstancesV2Request.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListBackendInstancesV2Request.

        页码

        :return: The offset of this ListBackendInstancesV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBackendInstancesV2Request.

        页码

        :param offset: The offset of this ListBackendInstancesV2Request.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, ListBackendInstancesV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
