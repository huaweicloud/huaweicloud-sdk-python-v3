# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VodInfoV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'play_url': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'play_url': 'play_url'
    }

    def __init__(self, asset_id=None, play_url=None):
        """VodInfoV2 - a model defined in huaweicloud sdk"""
        
        

        self._asset_id = None
        self._play_url = None
        self.discriminator = None

        self.asset_id = asset_id
        if play_url is not None:
            self.play_url = play_url

    @property
    def asset_id(self):
        """Gets the asset_id of this VodInfoV2.

        VOD媒资id

        :return: The asset_id of this VodInfoV2.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this VodInfoV2.

        VOD媒资id

        :param asset_id: The asset_id of this VodInfoV2.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def play_url(self):
        """Gets the play_url of this VodInfoV2.

        点播播放地址

        :return: The play_url of this VodInfoV2.
        :rtype: str
        """
        return self._play_url

    @play_url.setter
    def play_url(self, play_url):
        """Sets the play_url of this VodInfoV2.

        点播播放地址

        :param play_url: The play_url of this VodInfoV2.
        :type: str
        """
        self._play_url = play_url

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
        if not isinstance(other, VodInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other