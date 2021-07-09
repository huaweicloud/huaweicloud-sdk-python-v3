# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ConfirmCloudWafSubscriptionInfoResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'resources': 'list[CloudWafSubscriptioResponseResources]'
    }

    attribute_map = {
        'type': 'type',
        'resources': 'resources'
    }

    def __init__(self, type=None, resources=None):
        """ConfirmCloudWafSubscriptionInfoResponse - a model defined in huaweicloud sdk"""
        
        super(ConfirmCloudWafSubscriptionInfoResponse, self).__init__()

        self._type = None
        self._resources = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if resources is not None:
            self.resources = resources

    @property
    def type(self):
        """Gets the type of this ConfirmCloudWafSubscriptionInfoResponse.

        云模式版本，-2：已冻结，-1：未订购，1：基础版，2：专业版，3：企业版，4：旗舰版，22：按需版本

        :return: The type of this ConfirmCloudWafSubscriptionInfoResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfirmCloudWafSubscriptionInfoResponse.

        云模式版本，-2：已冻结，-1：未订购，1：基础版，2：专业版，3：企业版，4：旗舰版，22：按需版本

        :param type: The type of this ConfirmCloudWafSubscriptionInfoResponse.
        :type: int
        """
        self._type = type

    @property
    def resources(self):
        """Gets the resources of this ConfirmCloudWafSubscriptionInfoResponse.

        资源列表

        :return: The resources of this ConfirmCloudWafSubscriptionInfoResponse.
        :rtype: list[CloudWafSubscriptioResponseResources]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ConfirmCloudWafSubscriptionInfoResponse.

        资源列表

        :param resources: The resources of this ConfirmCloudWafSubscriptionInfoResponse.
        :type: list[CloudWafSubscriptioResponseResources]
        """
        self._resources = resources

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
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfirmCloudWafSubscriptionInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
