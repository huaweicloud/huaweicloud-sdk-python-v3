# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certs_records': 'CertsRecordsDatastore',
        'total_size': 'int'
    }

    attribute_map = {
        'certs_records': 'certsRecords',
        'total_size': 'totalSize'
    }

    def __init__(self, certs_records=None, total_size=None):
        r"""ListCertsResponse

        The model defined in huaweicloud sdk

        :param certs_records: 
        :type certs_records: :class:`huaweicloudsdkcss.v1.CertsRecordsDatastore`
        :param total_size: 证书记录数量。
        :type total_size: int
        """
        
        super(ListCertsResponse, self).__init__()

        self._certs_records = None
        self._total_size = None
        self.discriminator = None

        if certs_records is not None:
            self.certs_records = certs_records
        if total_size is not None:
            self.total_size = total_size

    @property
    def certs_records(self):
        r"""Gets the certs_records of this ListCertsResponse.

        :return: The certs_records of this ListCertsResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.CertsRecordsDatastore`
        """
        return self._certs_records

    @certs_records.setter
    def certs_records(self, certs_records):
        r"""Sets the certs_records of this ListCertsResponse.

        :param certs_records: The certs_records of this ListCertsResponse.
        :type certs_records: :class:`huaweicloudsdkcss.v1.CertsRecordsDatastore`
        """
        self._certs_records = certs_records

    @property
    def total_size(self):
        r"""Gets the total_size of this ListCertsResponse.

        证书记录数量。

        :return: The total_size of this ListCertsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListCertsResponse.

        证书记录数量。

        :param total_size: The total_size of this ListCertsResponse.
        :type total_size: int
        """
        self._total_size = total_size

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
        if not isinstance(other, ListCertsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
