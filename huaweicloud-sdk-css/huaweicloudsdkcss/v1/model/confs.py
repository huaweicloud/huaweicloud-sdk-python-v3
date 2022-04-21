# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Confs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'conf_content': 'str',
        'setting': 'Setting',
        'update_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'conf_content': 'confContent',
        'setting': 'setting',
        'update_at': 'updateAt'
    }

    def __init__(self, name=None, status=None, conf_content=None, setting=None, update_at=None):
        """Confs

        The model defined in huaweicloud sdk

        :param name: 配置文件名称。
        :type name: str
        :param status: 配置文件状态。
        :type status: str
        :param conf_content: 配置文件内容。
        :type conf_content: str
        :param setting: 
        :type setting: :class:`huaweicloudsdkcss.v1.Setting`
        :param update_at: 更新时间。
        :type update_at: str
        """
        
        

        self._name = None
        self._status = None
        self._conf_content = None
        self._setting = None
        self._update_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if conf_content is not None:
            self.conf_content = conf_content
        if setting is not None:
            self.setting = setting
        if update_at is not None:
            self.update_at = update_at

    @property
    def name(self):
        """Gets the name of this Confs.

        配置文件名称。

        :return: The name of this Confs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Confs.

        配置文件名称。

        :param name: The name of this Confs.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this Confs.

        配置文件状态。

        :return: The status of this Confs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Confs.

        配置文件状态。

        :param status: The status of this Confs.
        :type status: str
        """
        self._status = status

    @property
    def conf_content(self):
        """Gets the conf_content of this Confs.

        配置文件内容。

        :return: The conf_content of this Confs.
        :rtype: str
        """
        return self._conf_content

    @conf_content.setter
    def conf_content(self, conf_content):
        """Sets the conf_content of this Confs.

        配置文件内容。

        :param conf_content: The conf_content of this Confs.
        :type conf_content: str
        """
        self._conf_content = conf_content

    @property
    def setting(self):
        """Gets the setting of this Confs.


        :return: The setting of this Confs.
        :rtype: :class:`huaweicloudsdkcss.v1.Setting`
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        """Sets the setting of this Confs.


        :param setting: The setting of this Confs.
        :type setting: :class:`huaweicloudsdkcss.v1.Setting`
        """
        self._setting = setting

    @property
    def update_at(self):
        """Gets the update_at of this Confs.

        更新时间。

        :return: The update_at of this Confs.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this Confs.

        更新时间。

        :param update_at: The update_at of this Confs.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, Confs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
