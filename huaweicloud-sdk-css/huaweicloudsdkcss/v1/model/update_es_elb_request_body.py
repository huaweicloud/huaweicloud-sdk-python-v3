# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEsElbRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'agency': 'str',
        'elb_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'agency': 'agency',
        'elb_id': 'elb_id'
    }

    def __init__(self, enable=None, agency=None, elb_id=None):
        r"""UpdateEsElbRequestBody

        The model defined in huaweicloud sdk

        :param enable: 打开或关闭es负载均衡器。 - true：开启。 - false：关闭。
        :type enable: bool
        :param agency: 委托名称。
        :type agency: str
        :param elb_id: 负载均衡器id。
        :type elb_id: str
        """
        
        

        self._enable = None
        self._agency = None
        self._elb_id = None
        self.discriminator = None

        self.enable = enable
        if agency is not None:
            self.agency = agency
        if elb_id is not None:
            self.elb_id = elb_id

    @property
    def enable(self):
        r"""Gets the enable of this UpdateEsElbRequestBody.

        打开或关闭es负载均衡器。 - true：开启。 - false：关闭。

        :return: The enable of this UpdateEsElbRequestBody.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UpdateEsElbRequestBody.

        打开或关闭es负载均衡器。 - true：开启。 - false：关闭。

        :param enable: The enable of this UpdateEsElbRequestBody.
        :type enable: bool
        """
        self._enable = enable

    @property
    def agency(self):
        r"""Gets the agency of this UpdateEsElbRequestBody.

        委托名称。

        :return: The agency of this UpdateEsElbRequestBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this UpdateEsElbRequestBody.

        委托名称。

        :param agency: The agency of this UpdateEsElbRequestBody.
        :type agency: str
        """
        self._agency = agency

    @property
    def elb_id(self):
        r"""Gets the elb_id of this UpdateEsElbRequestBody.

        负载均衡器id。

        :return: The elb_id of this UpdateEsElbRequestBody.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this UpdateEsElbRequestBody.

        负载均衡器id。

        :param elb_id: The elb_id of this UpdateEsElbRequestBody.
        :type elb_id: str
        """
        self._elb_id = elb_id

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
        if not isinstance(other, UpdateEsElbRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
