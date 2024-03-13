# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrUpdateEntitiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'body': 'DataEntityWithExtInfo'
    }

    attribute_map = {
        'instance': 'instance',
        'body': 'body'
    }

    def __init__(self, instance=None, body=None):
        """CreateOrUpdateEntitiesRequest

        The model defined in huaweicloud sdk

        :param instance: 实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)
        :type instance: str
        :param body: Body of the CreateOrUpdateEntitiesRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.DataEntityWithExtInfo`
        """
        
        

        self._instance = None
        self._body = None
        self.discriminator = None

        self.instance = instance
        if body is not None:
            self.body = body

    @property
    def instance(self):
        """Gets the instance of this CreateOrUpdateEntitiesRequest.

        实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)

        :return: The instance of this CreateOrUpdateEntitiesRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this CreateOrUpdateEntitiesRequest.

        实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)

        :param instance: The instance of this CreateOrUpdateEntitiesRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def body(self):
        """Gets the body of this CreateOrUpdateEntitiesRequest.

        :return: The body of this CreateOrUpdateEntitiesRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataEntityWithExtInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateOrUpdateEntitiesRequest.

        :param body: The body of this CreateOrUpdateEntitiesRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.DataEntityWithExtInfo`
        """
        self._body = body

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
        if not isinstance(other, CreateOrUpdateEntitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
