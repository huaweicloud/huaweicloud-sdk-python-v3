# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeCbhRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'upgrade_time': 'int',
        'cancel': 'bool'
    }

    attribute_map = {
        'server_id': 'server_id',
        'upgrade_time': 'upgrade_time',
        'cancel': 'cancel'
    }

    def __init__(self, server_id=None, upgrade_time=None, cancel=None):
        r"""UpgradeCbhRequestBody

        The model defined in huaweicloud sdk

        :param server_id: 实例id
        :type server_id: str
        :param upgrade_time: 定时升级的时间，需要比当前时间大24小时
        :type upgrade_time: int
        :param cancel: 是否取消升级定时任务，已开始任务不可取消。 - true：取消 - false：无影响
        :type cancel: bool
        """
        
        

        self._server_id = None
        self._upgrade_time = None
        self._cancel = None
        self.discriminator = None

        self.server_id = server_id
        self.upgrade_time = upgrade_time
        if cancel is not None:
            self.cancel = cancel

    @property
    def server_id(self):
        r"""Gets the server_id of this UpgradeCbhRequestBody.

        实例id

        :return: The server_id of this UpgradeCbhRequestBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this UpgradeCbhRequestBody.

        实例id

        :param server_id: The server_id of this UpgradeCbhRequestBody.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def upgrade_time(self):
        r"""Gets the upgrade_time of this UpgradeCbhRequestBody.

        定时升级的时间，需要比当前时间大24小时

        :return: The upgrade_time of this UpgradeCbhRequestBody.
        :rtype: int
        """
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, upgrade_time):
        r"""Sets the upgrade_time of this UpgradeCbhRequestBody.

        定时升级的时间，需要比当前时间大24小时

        :param upgrade_time: The upgrade_time of this UpgradeCbhRequestBody.
        :type upgrade_time: int
        """
        self._upgrade_time = upgrade_time

    @property
    def cancel(self):
        r"""Gets the cancel of this UpgradeCbhRequestBody.

        是否取消升级定时任务，已开始任务不可取消。 - true：取消 - false：无影响

        :return: The cancel of this UpgradeCbhRequestBody.
        :rtype: bool
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        r"""Sets the cancel of this UpgradeCbhRequestBody.

        是否取消升级定时任务，已开始任务不可取消。 - true：取消 - false：无影响

        :param cancel: The cancel of this UpgradeCbhRequestBody.
        :type cancel: bool
        """
        self._cancel = cancel

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
        if not isinstance(other, UpgradeCbhRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
