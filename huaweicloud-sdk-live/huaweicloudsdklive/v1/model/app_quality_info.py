# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppQualityInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'quality_info': 'list[QualityInfo]'
    }

    attribute_map = {
        'app_name': 'app_name',
        'quality_info': 'quality_info'
    }

    def __init__(self, app_name=None, quality_info=None):
        """AppQualityInfo

        The model defined in huaweicloud sdk

        :param app_name: 应用名称
        :type app_name: str
        :param quality_info: 视频质量信息
        :type quality_info: list[:class:`huaweicloudsdklive.v1.QualityInfo`]
        """
        
        

        self._app_name = None
        self._quality_info = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if quality_info is not None:
            self.quality_info = quality_info

    @property
    def app_name(self):
        """Gets the app_name of this AppQualityInfo.

        应用名称

        :return: The app_name of this AppQualityInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppQualityInfo.

        应用名称

        :param app_name: The app_name of this AppQualityInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def quality_info(self):
        """Gets the quality_info of this AppQualityInfo.

        视频质量信息

        :return: The quality_info of this AppQualityInfo.
        :rtype: list[:class:`huaweicloudsdklive.v1.QualityInfo`]
        """
        return self._quality_info

    @quality_info.setter
    def quality_info(self, quality_info):
        """Sets the quality_info of this AppQualityInfo.

        视频质量信息

        :param quality_info: The quality_info of this AppQualityInfo.
        :type quality_info: list[:class:`huaweicloudsdklive.v1.QualityInfo`]
        """
        self._quality_info = quality_info

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
        if not isinstance(other, AppQualityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
