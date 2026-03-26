# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLockBlockingDbResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_list': 'list[str]'
    }

    attribute_map = {
        'db_list': 'db_list'
    }

    def __init__(self, db_list=None):
        r"""ListLockBlockingDbResponse

        The model defined in huaweicloud sdk

        :param db_list: 数据库名列表
        :type db_list: list[str]
        """
        
        super().__init__()

        self._db_list = None
        self.discriminator = None

        if db_list is not None:
            self.db_list = db_list

    @property
    def db_list(self):
        r"""Gets the db_list of this ListLockBlockingDbResponse.

        数据库名列表

        :return: The db_list of this ListLockBlockingDbResponse.
        :rtype: list[str]
        """
        return self._db_list

    @db_list.setter
    def db_list(self, db_list):
        r"""Sets the db_list of this ListLockBlockingDbResponse.

        数据库名列表

        :param db_list: The db_list of this ListLockBlockingDbResponse.
        :type db_list: list[str]
        """
        self._db_list = db_list

    def to_dict(self):
        import warnings
        warnings.warn("ListLockBlockingDbResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListLockBlockingDbResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
