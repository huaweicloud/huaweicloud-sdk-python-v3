# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRedislogDownloadLinkRequest:


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
        'id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'id': 'id'
    }

    def __init__(self, instance_id=None, id=None):
        """CreateRedislogDownloadLinkRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateRedislogDownloadLinkRequest.

        实例ID。

        :return: The instance_id of this CreateRedislogDownloadLinkRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateRedislogDownloadLinkRequest.

        实例ID。

        :param instance_id: The instance_id of this CreateRedislogDownloadLinkRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def id(self):
        """Gets the id of this CreateRedislogDownloadLinkRequest.

        日志的唯一ID，来自于查询运行日志查询接口

        :return: The id of this CreateRedislogDownloadLinkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRedislogDownloadLinkRequest.

        日志的唯一ID，来自于查询运行日志查询接口

        :param id: The id of this CreateRedislogDownloadLinkRequest.
        :type: str
        """
        self._id = id

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRedislogDownloadLinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other