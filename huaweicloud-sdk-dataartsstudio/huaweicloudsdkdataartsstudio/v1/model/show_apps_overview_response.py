# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppsOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apply_num': 'int',
        'call_num': 'int',
        'success_num': 'int',
        'fail_num': 'int',
        'legal_num': 'int',
        'illegal_num': 'int'
    }

    attribute_map = {
        'apply_num': 'apply_num',
        'call_num': 'call_num',
        'success_num': 'success_num',
        'fail_num': 'fail_num',
        'legal_num': 'legal_num',
        'illegal_num': 'illegal_num'
    }

    def __init__(self, apply_num=None, call_num=None, success_num=None, fail_num=None, legal_num=None, illegal_num=None):
        """ShowAppsOverviewResponse

        The model defined in huaweicloud sdk

        :param apply_num: 申请量
        :type apply_num: int
        :param call_num: 调用总量
        :type call_num: int
        :param success_num: 成功调用量(取数成功)
        :type success_num: int
        :param fail_num: 失败调用量(取数失败)
        :type fail_num: int
        :param legal_num: 合法调用量(通过校验)
        :type legal_num: int
        :param illegal_num: 非法调用量(无法通过校验)
        :type illegal_num: int
        """
        
        super(ShowAppsOverviewResponse, self).__init__()

        self._apply_num = None
        self._call_num = None
        self._success_num = None
        self._fail_num = None
        self._legal_num = None
        self._illegal_num = None
        self.discriminator = None

        if apply_num is not None:
            self.apply_num = apply_num
        if call_num is not None:
            self.call_num = call_num
        if success_num is not None:
            self.success_num = success_num
        if fail_num is not None:
            self.fail_num = fail_num
        if legal_num is not None:
            self.legal_num = legal_num
        if illegal_num is not None:
            self.illegal_num = illegal_num

    @property
    def apply_num(self):
        """Gets the apply_num of this ShowAppsOverviewResponse.

        申请量

        :return: The apply_num of this ShowAppsOverviewResponse.
        :rtype: int
        """
        return self._apply_num

    @apply_num.setter
    def apply_num(self, apply_num):
        """Sets the apply_num of this ShowAppsOverviewResponse.

        申请量

        :param apply_num: The apply_num of this ShowAppsOverviewResponse.
        :type apply_num: int
        """
        self._apply_num = apply_num

    @property
    def call_num(self):
        """Gets the call_num of this ShowAppsOverviewResponse.

        调用总量

        :return: The call_num of this ShowAppsOverviewResponse.
        :rtype: int
        """
        return self._call_num

    @call_num.setter
    def call_num(self, call_num):
        """Sets the call_num of this ShowAppsOverviewResponse.

        调用总量

        :param call_num: The call_num of this ShowAppsOverviewResponse.
        :type call_num: int
        """
        self._call_num = call_num

    @property
    def success_num(self):
        """Gets the success_num of this ShowAppsOverviewResponse.

        成功调用量(取数成功)

        :return: The success_num of this ShowAppsOverviewResponse.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this ShowAppsOverviewResponse.

        成功调用量(取数成功)

        :param success_num: The success_num of this ShowAppsOverviewResponse.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def fail_num(self):
        """Gets the fail_num of this ShowAppsOverviewResponse.

        失败调用量(取数失败)

        :return: The fail_num of this ShowAppsOverviewResponse.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        """Sets the fail_num of this ShowAppsOverviewResponse.

        失败调用量(取数失败)

        :param fail_num: The fail_num of this ShowAppsOverviewResponse.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def legal_num(self):
        """Gets the legal_num of this ShowAppsOverviewResponse.

        合法调用量(通过校验)

        :return: The legal_num of this ShowAppsOverviewResponse.
        :rtype: int
        """
        return self._legal_num

    @legal_num.setter
    def legal_num(self, legal_num):
        """Sets the legal_num of this ShowAppsOverviewResponse.

        合法调用量(通过校验)

        :param legal_num: The legal_num of this ShowAppsOverviewResponse.
        :type legal_num: int
        """
        self._legal_num = legal_num

    @property
    def illegal_num(self):
        """Gets the illegal_num of this ShowAppsOverviewResponse.

        非法调用量(无法通过校验)

        :return: The illegal_num of this ShowAppsOverviewResponse.
        :rtype: int
        """
        return self._illegal_num

    @illegal_num.setter
    def illegal_num(self, illegal_num):
        """Sets the illegal_num of this ShowAppsOverviewResponse.

        非法调用量(无法通过校验)

        :param illegal_num: The illegal_num of this ShowAppsOverviewResponse.
        :type illegal_num: int
        """
        self._illegal_num = illegal_num

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
        if not isinstance(other, ShowAppsOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
