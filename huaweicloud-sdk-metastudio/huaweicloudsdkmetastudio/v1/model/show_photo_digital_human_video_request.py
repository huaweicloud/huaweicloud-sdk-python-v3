# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPhotoDigitalHumanVideoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'x_app_user_id': 'str',
        'show_script': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_app_user_id': 'X-App-UserId',
        'show_script': 'show_script'
    }

    def __init__(self, job_id=None, x_app_user_id=None, show_script=None):
        """ShowPhotoDigitalHumanVideoRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param show_script: 是否需要返回剧本参数配置。
        :type show_script: bool
        """
        
        

        self._job_id = None
        self._x_app_user_id = None
        self._show_script = None
        self.discriminator = None

        self.job_id = job_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if show_script is not None:
            self.show_script = show_script

    @property
    def job_id(self):
        """Gets the job_id of this ShowPhotoDigitalHumanVideoRequest.

        任务ID。

        :return: The job_id of this ShowPhotoDigitalHumanVideoRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowPhotoDigitalHumanVideoRequest.

        任务ID。

        :param job_id: The job_id of this ShowPhotoDigitalHumanVideoRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this ShowPhotoDigitalHumanVideoRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this ShowPhotoDigitalHumanVideoRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this ShowPhotoDigitalHumanVideoRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this ShowPhotoDigitalHumanVideoRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def show_script(self):
        """Gets the show_script of this ShowPhotoDigitalHumanVideoRequest.

        是否需要返回剧本参数配置。

        :return: The show_script of this ShowPhotoDigitalHumanVideoRequest.
        :rtype: bool
        """
        return self._show_script

    @show_script.setter
    def show_script(self, show_script):
        """Sets the show_script of this ShowPhotoDigitalHumanVideoRequest.

        是否需要返回剧本参数配置。

        :param show_script: The show_script of this ShowPhotoDigitalHumanVideoRequest.
        :type show_script: bool
        """
        self._show_script = show_script

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
        if not isinstance(other, ShowPhotoDigitalHumanVideoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
