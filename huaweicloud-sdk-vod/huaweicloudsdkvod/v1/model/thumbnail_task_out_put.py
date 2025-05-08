# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThumbnailTaskOutPut:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_info': 'ObsInfo',
        'pic_info_list': 'list[PicInfo]'
    }

    attribute_map = {
        'obs_info': 'obs_info',
        'pic_info_list': 'pic_info_list'
    }

    def __init__(self, obs_info=None, pic_info_list=None):
        r"""ThumbnailTaskOutPut

        The model defined in huaweicloud sdk

        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param pic_info_list: 截图信息列表
        :type pic_info_list: list[:class:`huaweicloudsdkvod.v1.PicInfo`]
        """
        
        

        self._obs_info = None
        self._pic_info_list = None
        self.discriminator = None

        if obs_info is not None:
            self.obs_info = obs_info
        if pic_info_list is not None:
            self.pic_info_list = pic_info_list

    @property
    def obs_info(self):
        r"""Gets the obs_info of this ThumbnailTaskOutPut.

        :return: The obs_info of this ThumbnailTaskOutPut.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        r"""Sets the obs_info of this ThumbnailTaskOutPut.

        :param obs_info: The obs_info of this ThumbnailTaskOutPut.
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._obs_info = obs_info

    @property
    def pic_info_list(self):
        r"""Gets the pic_info_list of this ThumbnailTaskOutPut.

        截图信息列表

        :return: The pic_info_list of this ThumbnailTaskOutPut.
        :rtype: list[:class:`huaweicloudsdkvod.v1.PicInfo`]
        """
        return self._pic_info_list

    @pic_info_list.setter
    def pic_info_list(self, pic_info_list):
        r"""Sets the pic_info_list of this ThumbnailTaskOutPut.

        截图信息列表

        :param pic_info_list: The pic_info_list of this ThumbnailTaskOutPut.
        :type pic_info_list: list[:class:`huaweicloudsdkvod.v1.PicInfo`]
        """
        self._pic_info_list = pic_info_list

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
        if not isinstance(other, ThumbnailTaskOutPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
