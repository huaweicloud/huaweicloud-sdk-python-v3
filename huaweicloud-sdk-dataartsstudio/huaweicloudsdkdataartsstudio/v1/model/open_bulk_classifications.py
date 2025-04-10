# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenBulkClassifications:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'guids': 'list[str]',
        'classification': 'OpenClassification'
    }

    attribute_map = {
        'guids': 'guids',
        'classification': 'classification'
    }

    def __init__(self, guids=None, classification=None):
        r"""OpenBulkClassifications

        The model defined in huaweicloud sdk

        :param guids: 数据资产list
        :type guids: list[str]
        :param classification: 
        :type classification: :class:`huaweicloudsdkdataartsstudio.v1.OpenClassification`
        """
        
        

        self._guids = None
        self._classification = None
        self.discriminator = None

        self.guids = guids
        self.classification = classification

    @property
    def guids(self):
        r"""Gets the guids of this OpenBulkClassifications.

        数据资产list

        :return: The guids of this OpenBulkClassifications.
        :rtype: list[str]
        """
        return self._guids

    @guids.setter
    def guids(self, guids):
        r"""Sets the guids of this OpenBulkClassifications.

        数据资产list

        :param guids: The guids of this OpenBulkClassifications.
        :type guids: list[str]
        """
        self._guids = guids

    @property
    def classification(self):
        r"""Gets the classification of this OpenBulkClassifications.

        :return: The classification of this OpenBulkClassifications.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.OpenClassification`
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        r"""Sets the classification of this OpenBulkClassifications.

        :param classification: The classification of this OpenBulkClassifications.
        :type classification: :class:`huaweicloudsdkdataartsstudio.v1.OpenClassification`
        """
        self._classification = classification

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
        if not isinstance(other, OpenBulkClassifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
