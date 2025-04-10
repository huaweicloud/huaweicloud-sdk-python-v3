# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'reserve_obs_file': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'reserve_obs_file': 'reserve_obs_file'
    }

    def __init__(self, app_id=None, reserve_obs_file=None):
        r"""DeleteAppRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用ID。
        :type app_id: str
        :param reserve_obs_file: 删除应用时是否保留OBS桶文件(默认false) * &#39;true&#39; - 保留OBS桶文件,仅删除应用 * &#39;false&#39; - 不保留OBS桶文件,删除应用同时删除OBS桶文件
        :type reserve_obs_file: str
        """
        
        

        self._app_id = None
        self._reserve_obs_file = None
        self.discriminator = None

        self.app_id = app_id
        if reserve_obs_file is not None:
            self.reserve_obs_file = reserve_obs_file

    @property
    def app_id(self):
        r"""Gets the app_id of this DeleteAppRequest.

        应用ID。

        :return: The app_id of this DeleteAppRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this DeleteAppRequest.

        应用ID。

        :param app_id: The app_id of this DeleteAppRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def reserve_obs_file(self):
        r"""Gets the reserve_obs_file of this DeleteAppRequest.

        删除应用时是否保留OBS桶文件(默认false) * 'true' - 保留OBS桶文件,仅删除应用 * 'false' - 不保留OBS桶文件,删除应用同时删除OBS桶文件

        :return: The reserve_obs_file of this DeleteAppRequest.
        :rtype: str
        """
        return self._reserve_obs_file

    @reserve_obs_file.setter
    def reserve_obs_file(self, reserve_obs_file):
        r"""Sets the reserve_obs_file of this DeleteAppRequest.

        删除应用时是否保留OBS桶文件(默认false) * 'true' - 保留OBS桶文件,仅删除应用 * 'false' - 不保留OBS桶文件,删除应用同时删除OBS桶文件

        :param reserve_obs_file: The reserve_obs_file of this DeleteAppRequest.
        :type reserve_obs_file: str
        """
        self._reserve_obs_file = reserve_obs_file

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
        if not isinstance(other, DeleteAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
