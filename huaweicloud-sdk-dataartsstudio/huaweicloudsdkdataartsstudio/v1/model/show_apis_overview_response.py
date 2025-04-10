# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApisOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_num': 'int',
        'developing_num': 'int',
        'apply_num': 'int',
        'call_num': 'int',
        'success_num': 'int',
        'fail_num': 'int',
        'legal_num': 'int',
        'illegal_num': 'int'
    }

    attribute_map = {
        'publish_num': 'publish_num',
        'developing_num': 'developing_num',
        'apply_num': 'apply_num',
        'call_num': 'call_num',
        'success_num': 'success_num',
        'fail_num': 'fail_num',
        'legal_num': 'legal_num',
        'illegal_num': 'illegal_num'
    }

    def __init__(self, publish_num=None, developing_num=None, apply_num=None, call_num=None, success_num=None, fail_num=None, legal_num=None, illegal_num=None):
        r"""ShowApisOverviewResponse

        The model defined in huaweicloud sdk

        :param publish_num: 已发布API量
        :type publish_num: int
        :param developing_num: 开发中API量
        :type developing_num: int
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
        
        super(ShowApisOverviewResponse, self).__init__()

        self._publish_num = None
        self._developing_num = None
        self._apply_num = None
        self._call_num = None
        self._success_num = None
        self._fail_num = None
        self._legal_num = None
        self._illegal_num = None
        self.discriminator = None

        if publish_num is not None:
            self.publish_num = publish_num
        if developing_num is not None:
            self.developing_num = developing_num
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
    def publish_num(self):
        r"""Gets the publish_num of this ShowApisOverviewResponse.

        已发布API量

        :return: The publish_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._publish_num

    @publish_num.setter
    def publish_num(self, publish_num):
        r"""Sets the publish_num of this ShowApisOverviewResponse.

        已发布API量

        :param publish_num: The publish_num of this ShowApisOverviewResponse.
        :type publish_num: int
        """
        self._publish_num = publish_num

    @property
    def developing_num(self):
        r"""Gets the developing_num of this ShowApisOverviewResponse.

        开发中API量

        :return: The developing_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._developing_num

    @developing_num.setter
    def developing_num(self, developing_num):
        r"""Sets the developing_num of this ShowApisOverviewResponse.

        开发中API量

        :param developing_num: The developing_num of this ShowApisOverviewResponse.
        :type developing_num: int
        """
        self._developing_num = developing_num

    @property
    def apply_num(self):
        r"""Gets the apply_num of this ShowApisOverviewResponse.

        申请量

        :return: The apply_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._apply_num

    @apply_num.setter
    def apply_num(self, apply_num):
        r"""Sets the apply_num of this ShowApisOverviewResponse.

        申请量

        :param apply_num: The apply_num of this ShowApisOverviewResponse.
        :type apply_num: int
        """
        self._apply_num = apply_num

    @property
    def call_num(self):
        r"""Gets the call_num of this ShowApisOverviewResponse.

        调用总量

        :return: The call_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._call_num

    @call_num.setter
    def call_num(self, call_num):
        r"""Sets the call_num of this ShowApisOverviewResponse.

        调用总量

        :param call_num: The call_num of this ShowApisOverviewResponse.
        :type call_num: int
        """
        self._call_num = call_num

    @property
    def success_num(self):
        r"""Gets the success_num of this ShowApisOverviewResponse.

        成功调用量(取数成功)

        :return: The success_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this ShowApisOverviewResponse.

        成功调用量(取数成功)

        :param success_num: The success_num of this ShowApisOverviewResponse.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def fail_num(self):
        r"""Gets the fail_num of this ShowApisOverviewResponse.

        失败调用量(取数失败)

        :return: The fail_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        r"""Sets the fail_num of this ShowApisOverviewResponse.

        失败调用量(取数失败)

        :param fail_num: The fail_num of this ShowApisOverviewResponse.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def legal_num(self):
        r"""Gets the legal_num of this ShowApisOverviewResponse.

        合法调用量(通过校验)

        :return: The legal_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._legal_num

    @legal_num.setter
    def legal_num(self, legal_num):
        r"""Sets the legal_num of this ShowApisOverviewResponse.

        合法调用量(通过校验)

        :param legal_num: The legal_num of this ShowApisOverviewResponse.
        :type legal_num: int
        """
        self._legal_num = legal_num

    @property
    def illegal_num(self):
        r"""Gets the illegal_num of this ShowApisOverviewResponse.

        非法调用量(无法通过校验)

        :return: The illegal_num of this ShowApisOverviewResponse.
        :rtype: int
        """
        return self._illegal_num

    @illegal_num.setter
    def illegal_num(self, illegal_num):
        r"""Sets the illegal_num of this ShowApisOverviewResponse.

        非法调用量(无法通过校验)

        :param illegal_num: The illegal_num of this ShowApisOverviewResponse.
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
        if not isinstance(other, ShowApisOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
