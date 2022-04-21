# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeLifecycleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pre_install': 'str',
        'post_install': 'str'
    }

    attribute_map = {
        'pre_install': 'preInstall',
        'post_install': 'postInstall'
    }

    def __init__(self, pre_install=None, post_install=None):
        """NodeLifecycleConfig

        The model defined in huaweicloud sdk

        :param pre_install: 安装前执行脚本 &gt; 输入的值需要经过Base64编码，方法为echo -n \&quot;待编码内容\&quot; | base64。 
        :type pre_install: str
        :param post_install: 安装后执行脚本 &gt; 输入的值需要经过Base64编码，方法为echo -n \&quot;待编码内容\&quot; | base64。 
        :type post_install: str
        """
        
        

        self._pre_install = None
        self._post_install = None
        self.discriminator = None

        if pre_install is not None:
            self.pre_install = pre_install
        if post_install is not None:
            self.post_install = post_install

    @property
    def pre_install(self):
        """Gets the pre_install of this NodeLifecycleConfig.

        安装前执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :return: The pre_install of this NodeLifecycleConfig.
        :rtype: str
        """
        return self._pre_install

    @pre_install.setter
    def pre_install(self, pre_install):
        """Sets the pre_install of this NodeLifecycleConfig.

        安装前执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :param pre_install: The pre_install of this NodeLifecycleConfig.
        :type pre_install: str
        """
        self._pre_install = pre_install

    @property
    def post_install(self):
        """Gets the post_install of this NodeLifecycleConfig.

        安装后执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :return: The post_install of this NodeLifecycleConfig.
        :rtype: str
        """
        return self._post_install

    @post_install.setter
    def post_install(self, post_install):
        """Sets the post_install of this NodeLifecycleConfig.

        安装后执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :param post_install: The post_install of this NodeLifecycleConfig.
        :type post_install: str
        """
        self._post_install = post_install

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
        if not isinstance(other, NodeLifecycleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
