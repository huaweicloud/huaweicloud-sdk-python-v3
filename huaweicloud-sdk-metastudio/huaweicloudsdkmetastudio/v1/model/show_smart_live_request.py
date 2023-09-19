# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmartLiveRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'job_id': 'str',
        'x_app_user_id': 'str'
    }

    attribute_map = {
        'room_id': 'room_id',
        'job_id': 'job_id',
        'x_app_user_id': 'X-App-UserId'
    }

    def __init__(self, room_id=None, job_id=None, x_app_user_id=None):
        """ShowSmartLiveRequest

        The model defined in huaweicloud sdk

        :param room_id: 剧本ID。
        :type room_id: str
        :param job_id: 任务ID。
        :type job_id: str
        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        """
        
        

        self._room_id = None
        self._job_id = None
        self._x_app_user_id = None
        self.discriminator = None

        self.room_id = room_id
        self.job_id = job_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id

    @property
    def room_id(self):
        """Gets the room_id of this ShowSmartLiveRequest.

        剧本ID。

        :return: The room_id of this ShowSmartLiveRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ShowSmartLiveRequest.

        剧本ID。

        :param room_id: The room_id of this ShowSmartLiveRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def job_id(self):
        """Gets the job_id of this ShowSmartLiveRequest.

        任务ID。

        :return: The job_id of this ShowSmartLiveRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowSmartLiveRequest.

        任务ID。

        :param job_id: The job_id of this ShowSmartLiveRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this ShowSmartLiveRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this ShowSmartLiveRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this ShowSmartLiveRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this ShowSmartLiveRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

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
        if not isinstance(other, ShowSmartLiveRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
