# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRegistryStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fail_num': 'int',
        'success_num': 'int'
    }

    attribute_map = {
        'fail_num': 'fail_num',
        'success_num': 'success_num'
    }

    def __init__(self, fail_num=None, success_num=None):
        r"""ListRegistryStatisticsResponse

        The model defined in huaweicloud sdk

        :param fail_num: **参数解释**： 接入异常数量 **取值范围**： 0-100 
        :type fail_num: int
        :param success_num: **参数解释**： 接入成功数量 **取值范围**： 0-100 
        :type success_num: int
        """
        
        super(ListRegistryStatisticsResponse, self).__init__()

        self._fail_num = None
        self._success_num = None
        self.discriminator = None

        if fail_num is not None:
            self.fail_num = fail_num
        if success_num is not None:
            self.success_num = success_num

    @property
    def fail_num(self):
        r"""Gets the fail_num of this ListRegistryStatisticsResponse.

        **参数解释**： 接入异常数量 **取值范围**： 0-100 

        :return: The fail_num of this ListRegistryStatisticsResponse.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        r"""Sets the fail_num of this ListRegistryStatisticsResponse.

        **参数解释**： 接入异常数量 **取值范围**： 0-100 

        :param fail_num: The fail_num of this ListRegistryStatisticsResponse.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def success_num(self):
        r"""Gets the success_num of this ListRegistryStatisticsResponse.

        **参数解释**： 接入成功数量 **取值范围**： 0-100 

        :return: The success_num of this ListRegistryStatisticsResponse.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this ListRegistryStatisticsResponse.

        **参数解释**： 接入成功数量 **取值范围**： 0-100 

        :param success_num: The success_num of this ListRegistryStatisticsResponse.
        :type success_num: int
        """
        self._success_num = success_num

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
        if not isinstance(other, ListRegistryStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
