# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCasesStatusResponseV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cases_status_ja': 'list[object]'
    }

    attribute_map = {
        'cases_status_ja': 'casesStatusJA'
    }

    def __init__(self, cases_status_ja=None):
        r"""QueryCasesStatusResponseV2

        The model defined in huaweicloud sdk

        :param cases_status_ja: 
        :type cases_status_ja: list[object]
        """
        
        

        self._cases_status_ja = None
        self.discriminator = None

        if cases_status_ja is not None:
            self.cases_status_ja = cases_status_ja

    @property
    def cases_status_ja(self):
        r"""Gets the cases_status_ja of this QueryCasesStatusResponseV2.

        :return: The cases_status_ja of this QueryCasesStatusResponseV2.
        :rtype: list[object]
        """
        return self._cases_status_ja

    @cases_status_ja.setter
    def cases_status_ja(self, cases_status_ja):
        r"""Sets the cases_status_ja of this QueryCasesStatusResponseV2.

        :param cases_status_ja: The cases_status_ja of this QueryCasesStatusResponseV2.
        :type cases_status_ja: list[object]
        """
        self._cases_status_ja = cases_status_ja

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
        if not isinstance(other, QueryCasesStatusResponseV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
