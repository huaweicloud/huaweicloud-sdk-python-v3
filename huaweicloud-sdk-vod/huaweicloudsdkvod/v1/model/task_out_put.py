# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskOutPut:

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
        'meta_data': 'ObjectMetaData',
        'file_url': 'str'
    }

    attribute_map = {
        'obs_info': 'obs_info',
        'meta_data': 'meta_data',
        'file_url': 'file_url'
    }

    def __init__(self, obs_info=None, meta_data=None, file_url=None):
        r"""TaskOutPut

        The model defined in huaweicloud sdk

        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        :param file_url: 输出文件播放地址
        :type file_url: str
        """
        
        

        self._obs_info = None
        self._meta_data = None
        self._file_url = None
        self.discriminator = None

        if obs_info is not None:
            self.obs_info = obs_info
        if meta_data is not None:
            self.meta_data = meta_data
        if file_url is not None:
            self.file_url = file_url

    @property
    def obs_info(self):
        r"""Gets the obs_info of this TaskOutPut.

        :return: The obs_info of this TaskOutPut.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        r"""Sets the obs_info of this TaskOutPut.

        :param obs_info: The obs_info of this TaskOutPut.
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._obs_info = obs_info

    @property
    def meta_data(self):
        r"""Gets the meta_data of this TaskOutPut.

        :return: The meta_data of this TaskOutPut.
        :rtype: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this TaskOutPut.

        :param meta_data: The meta_data of this TaskOutPut.
        :type meta_data: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        self._meta_data = meta_data

    @property
    def file_url(self):
        r"""Gets the file_url of this TaskOutPut.

        输出文件播放地址

        :return: The file_url of this TaskOutPut.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        r"""Sets the file_url of this TaskOutPut.

        输出文件播放地址

        :param file_url: The file_url of this TaskOutPut.
        :type file_url: str
        """
        self._file_url = file_url

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
        if not isinstance(other, TaskOutPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
