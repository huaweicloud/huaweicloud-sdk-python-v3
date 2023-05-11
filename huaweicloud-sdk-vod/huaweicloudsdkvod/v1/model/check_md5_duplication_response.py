# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckMd5DuplicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_duplicated': 'int',
        'asset_ids': 'list[str]'
    }

    attribute_map = {
        'is_duplicated': 'is_duplicated',
        'asset_ids': 'asset_ids'
    }

    def __init__(self, is_duplicated=None, asset_ids=None):
        """CheckMd5DuplicationResponse

        The model defined in huaweicloud sdk

        :param is_duplicated: 是否重复。  取值如下： - 0：表示不重复。 - 1：表示重复。
        :type is_duplicated: int
        :param asset_ids: 重复的媒资ID
        :type asset_ids: list[str]
        """
        
        super(CheckMd5DuplicationResponse, self).__init__()

        self._is_duplicated = None
        self._asset_ids = None
        self.discriminator = None

        if is_duplicated is not None:
            self.is_duplicated = is_duplicated
        if asset_ids is not None:
            self.asset_ids = asset_ids

    @property
    def is_duplicated(self):
        """Gets the is_duplicated of this CheckMd5DuplicationResponse.

        是否重复。  取值如下： - 0：表示不重复。 - 1：表示重复。

        :return: The is_duplicated of this CheckMd5DuplicationResponse.
        :rtype: int
        """
        return self._is_duplicated

    @is_duplicated.setter
    def is_duplicated(self, is_duplicated):
        """Sets the is_duplicated of this CheckMd5DuplicationResponse.

        是否重复。  取值如下： - 0：表示不重复。 - 1：表示重复。

        :param is_duplicated: The is_duplicated of this CheckMd5DuplicationResponse.
        :type is_duplicated: int
        """
        self._is_duplicated = is_duplicated

    @property
    def asset_ids(self):
        """Gets the asset_ids of this CheckMd5DuplicationResponse.

        重复的媒资ID

        :return: The asset_ids of this CheckMd5DuplicationResponse.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """Sets the asset_ids of this CheckMd5DuplicationResponse.

        重复的媒资ID

        :param asset_ids: The asset_ids of this CheckMd5DuplicationResponse.
        :type asset_ids: list[str]
        """
        self._asset_ids = asset_ids

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
        if not isinstance(other, CheckMd5DuplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
