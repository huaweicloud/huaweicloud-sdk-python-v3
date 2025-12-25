# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRetrieveScriptsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listcount': 'int',
        'records': 'list[RetrieveScript]'
    }

    attribute_map = {
        'listcount': 'listcount',
        'records': 'records'
    }

    def __init__(self, listcount=None, records=None):
        r"""ListRetrieveScriptsResponse

        The model defined in huaweicloud sdk

        :param listcount: 计数
        :type listcount: int
        :param records: 检索
        :type records: list[:class:`huaweicloudsdksecmaster.v2.RetrieveScript`]
        """
        
        super().__init__()

        self._listcount = None
        self._records = None
        self.discriminator = None

        if listcount is not None:
            self.listcount = listcount
        if records is not None:
            self.records = records

    @property
    def listcount(self):
        r"""Gets the listcount of this ListRetrieveScriptsResponse.

        计数

        :return: The listcount of this ListRetrieveScriptsResponse.
        :rtype: int
        """
        return self._listcount

    @listcount.setter
    def listcount(self, listcount):
        r"""Sets the listcount of this ListRetrieveScriptsResponse.

        计数

        :param listcount: The listcount of this ListRetrieveScriptsResponse.
        :type listcount: int
        """
        self._listcount = listcount

    @property
    def records(self):
        r"""Gets the records of this ListRetrieveScriptsResponse.

        检索

        :return: The records of this ListRetrieveScriptsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.RetrieveScript`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListRetrieveScriptsResponse.

        检索

        :param records: The records of this ListRetrieveScriptsResponse.
        :type records: list[:class:`huaweicloudsdksecmaster.v2.RetrieveScript`]
        """
        self._records = records

    def to_dict(self):
        import warnings
        warnings.warn("ListRetrieveScriptsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListRetrieveScriptsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
