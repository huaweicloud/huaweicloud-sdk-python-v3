# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowCaseStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'int'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):
        """ShowCaseStatusResponse - a model defined in huaweicloud sdk"""
        
        super(ShowCaseStatusResponse, self).__init__()

        self._status = None
        self.discriminator = None

        if status is not None:
            self.status = status

    @property
    def status(self):
        """Gets the status of this ShowCaseStatusResponse.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :return: The status of this ShowCaseStatusResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowCaseStatusResponse.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :param status: The status of this ShowCaseStatusResponse.
        :type: int
        """
        self._status = status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowCaseStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other