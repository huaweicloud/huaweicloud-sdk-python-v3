# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataProfileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'ProfileInfo',
        'rowkey': 'str',
        'status': 'str'
    }

    attribute_map = {
        'data': 'data',
        'rowkey': 'rowkey',
        'status': 'status'
    }

    def __init__(self, data=None, rowkey=None, status=None):
        r"""ShowDataProfileResponse

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkdataartsstudio.v1.ProfileInfo`
        :param rowkey: 行键
        :type rowkey: str
        :param status: 状态
        :type status: str
        """
        
        super(ShowDataProfileResponse, self).__init__()

        self._data = None
        self._rowkey = None
        self._status = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if rowkey is not None:
            self.rowkey = rowkey
        if status is not None:
            self.status = status

    @property
    def data(self):
        r"""Gets the data of this ShowDataProfileResponse.

        :return: The data of this ShowDataProfileResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ProfileInfo`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowDataProfileResponse.

        :param data: The data of this ShowDataProfileResponse.
        :type data: :class:`huaweicloudsdkdataartsstudio.v1.ProfileInfo`
        """
        self._data = data

    @property
    def rowkey(self):
        r"""Gets the rowkey of this ShowDataProfileResponse.

        行键

        :return: The rowkey of this ShowDataProfileResponse.
        :rtype: str
        """
        return self._rowkey

    @rowkey.setter
    def rowkey(self, rowkey):
        r"""Sets the rowkey of this ShowDataProfileResponse.

        行键

        :param rowkey: The rowkey of this ShowDataProfileResponse.
        :type rowkey: str
        """
        self._rowkey = rowkey

    @property
    def status(self):
        r"""Gets the status of this ShowDataProfileResponse.

        状态

        :return: The status of this ShowDataProfileResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDataProfileResponse.

        状态

        :param status: The status of this ShowDataProfileResponse.
        :type status: str
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
        if not isinstance(other, ShowDataProfileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
