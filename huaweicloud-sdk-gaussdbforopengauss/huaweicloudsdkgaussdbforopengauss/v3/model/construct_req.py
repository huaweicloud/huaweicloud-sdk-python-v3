# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConstructReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_type': 'str',
        'dr_ip': 'str',
        'dr_user_name': 'str',
        'dr_user_password': 'str',
        'dr_task_name': 'str'
    }

    attribute_map = {
        'disaster_type': 'disaster_type',
        'dr_ip': 'dr_ip',
        'dr_user_name': 'dr_user_name',
        'dr_user_password': 'dr_user_password',
        'dr_task_name': 'dr_task_name'
    }

    def __init__(self, disaster_type=None, dr_ip=None, dr_user_name=None, dr_user_password=None, dr_task_name=None):
        r"""ConstructReq

        The model defined in huaweicloud sdk

        :param disaster_type: 容灾类型。
        :type disaster_type: str
        :param dr_ip: 对端实例任意数据ip。
        :type dr_ip: str
        :param dr_user_name: 对端实例账户名称。
        :type dr_user_name: str
        :param dr_user_password: 对端实例账户密码。
        :type dr_user_password: str
        :param dr_task_name: 容灾任务名称
        :type dr_task_name: str
        """
        
        

        self._disaster_type = None
        self._dr_ip = None
        self._dr_user_name = None
        self._dr_user_password = None
        self._dr_task_name = None
        self.discriminator = None

        self.disaster_type = disaster_type
        self.dr_ip = dr_ip
        self.dr_user_name = dr_user_name
        self.dr_user_password = dr_user_password
        if dr_task_name is not None:
            self.dr_task_name = dr_task_name

    @property
    def disaster_type(self):
        r"""Gets the disaster_type of this ConstructReq.

        容灾类型。

        :return: The disaster_type of this ConstructReq.
        :rtype: str
        """
        return self._disaster_type

    @disaster_type.setter
    def disaster_type(self, disaster_type):
        r"""Sets the disaster_type of this ConstructReq.

        容灾类型。

        :param disaster_type: The disaster_type of this ConstructReq.
        :type disaster_type: str
        """
        self._disaster_type = disaster_type

    @property
    def dr_ip(self):
        r"""Gets the dr_ip of this ConstructReq.

        对端实例任意数据ip。

        :return: The dr_ip of this ConstructReq.
        :rtype: str
        """
        return self._dr_ip

    @dr_ip.setter
    def dr_ip(self, dr_ip):
        r"""Sets the dr_ip of this ConstructReq.

        对端实例任意数据ip。

        :param dr_ip: The dr_ip of this ConstructReq.
        :type dr_ip: str
        """
        self._dr_ip = dr_ip

    @property
    def dr_user_name(self):
        r"""Gets the dr_user_name of this ConstructReq.

        对端实例账户名称。

        :return: The dr_user_name of this ConstructReq.
        :rtype: str
        """
        return self._dr_user_name

    @dr_user_name.setter
    def dr_user_name(self, dr_user_name):
        r"""Sets the dr_user_name of this ConstructReq.

        对端实例账户名称。

        :param dr_user_name: The dr_user_name of this ConstructReq.
        :type dr_user_name: str
        """
        self._dr_user_name = dr_user_name

    @property
    def dr_user_password(self):
        r"""Gets the dr_user_password of this ConstructReq.

        对端实例账户密码。

        :return: The dr_user_password of this ConstructReq.
        :rtype: str
        """
        return self._dr_user_password

    @dr_user_password.setter
    def dr_user_password(self, dr_user_password):
        r"""Sets the dr_user_password of this ConstructReq.

        对端实例账户密码。

        :param dr_user_password: The dr_user_password of this ConstructReq.
        :type dr_user_password: str
        """
        self._dr_user_password = dr_user_password

    @property
    def dr_task_name(self):
        r"""Gets the dr_task_name of this ConstructReq.

        容灾任务名称

        :return: The dr_task_name of this ConstructReq.
        :rtype: str
        """
        return self._dr_task_name

    @dr_task_name.setter
    def dr_task_name(self, dr_task_name):
        r"""Sets the dr_task_name of this ConstructReq.

        容灾任务名称

        :param dr_task_name: The dr_task_name of this ConstructReq.
        :type dr_task_name: str
        """
        self._dr_task_name = dr_task_name

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
        if not isinstance(other, ConstructReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
