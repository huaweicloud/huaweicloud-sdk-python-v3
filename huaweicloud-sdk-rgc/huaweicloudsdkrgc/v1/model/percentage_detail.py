# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PercentageDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'percentage_name': 'str',
        'percentage_status': 'str'
    }

    attribute_map = {
        'percentage_name': 'percentage_name',
        'percentage_status': 'percentage_status'
    }

    def __init__(self, percentage_name=None, percentage_status=None):
        r"""PercentageDetail

        The model defined in huaweicloud sdk

        :param percentage_name: 进度名称。
        :type percentage_name: str
        :param percentage_status: 进度状态。
        :type percentage_status: str
        """
        
        

        self._percentage_name = None
        self._percentage_status = None
        self.discriminator = None

        if percentage_name is not None:
            self.percentage_name = percentage_name
        if percentage_status is not None:
            self.percentage_status = percentage_status

    @property
    def percentage_name(self):
        r"""Gets the percentage_name of this PercentageDetail.

        进度名称。

        :return: The percentage_name of this PercentageDetail.
        :rtype: str
        """
        return self._percentage_name

    @percentage_name.setter
    def percentage_name(self, percentage_name):
        r"""Sets the percentage_name of this PercentageDetail.

        进度名称。

        :param percentage_name: The percentage_name of this PercentageDetail.
        :type percentage_name: str
        """
        self._percentage_name = percentage_name

    @property
    def percentage_status(self):
        r"""Gets the percentage_status of this PercentageDetail.

        进度状态。

        :return: The percentage_status of this PercentageDetail.
        :rtype: str
        """
        return self._percentage_status

    @percentage_status.setter
    def percentage_status(self, percentage_status):
        r"""Sets the percentage_status of this PercentageDetail.

        进度状态。

        :param percentage_status: The percentage_status of this PercentageDetail.
        :type percentage_status: str
        """
        self._percentage_status = percentage_status

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
        if not isinstance(other, PercentageDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
