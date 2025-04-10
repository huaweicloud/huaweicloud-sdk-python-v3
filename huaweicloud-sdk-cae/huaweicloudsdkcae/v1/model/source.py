# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Source:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'Repo',
        'type': 'str',
        'sub_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'code': 'code',
        'type': 'type',
        'sub_type': 'sub_type',
        'url': 'url'
    }

    def __init__(self, code=None, type=None, sub_type=None, url=None):
        r"""Source

        The model defined in huaweicloud sdk

        :param code: 
        :type code: :class:`huaweicloudsdkcae.v1.Repo`
        :param type: 源类型。
        :type type: str
        :param sub_type: 源子类型。 - 源类型为code时，子类型表示不同的代码仓库，如DevCloud（CodeArts）、GitLab、GitHub、Gitee、Bitbucket。 - 源类型为softwarePackage时，子类型表示不同的软件包仓库，如BinObs、BinDevCloud（CodeArts软件发布库）。
        :type sub_type: str
        :param url: url地址。 - 源类型为image时，url地址为镜像地址。 - 源类型为code时，url地址为git地址。 - 源类型为softwarePackage时，url地址为软件包地址。
        :type url: str
        """
        
        

        self._code = None
        self._type = None
        self._sub_type = None
        self._url = None
        self.discriminator = None

        if code is not None:
            self.code = code
        self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        self.url = url

    @property
    def code(self):
        r"""Gets the code of this Source.

        :return: The code of this Source.
        :rtype: :class:`huaweicloudsdkcae.v1.Repo`
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Source.

        :param code: The code of this Source.
        :type code: :class:`huaweicloudsdkcae.v1.Repo`
        """
        self._code = code

    @property
    def type(self):
        r"""Gets the type of this Source.

        源类型。

        :return: The type of this Source.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Source.

        源类型。

        :param type: The type of this Source.
        :type type: str
        """
        self._type = type

    @property
    def sub_type(self):
        r"""Gets the sub_type of this Source.

        源子类型。 - 源类型为code时，子类型表示不同的代码仓库，如DevCloud（CodeArts）、GitLab、GitHub、Gitee、Bitbucket。 - 源类型为softwarePackage时，子类型表示不同的软件包仓库，如BinObs、BinDevCloud（CodeArts软件发布库）。

        :return: The sub_type of this Source.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this Source.

        源子类型。 - 源类型为code时，子类型表示不同的代码仓库，如DevCloud（CodeArts）、GitLab、GitHub、Gitee、Bitbucket。 - 源类型为softwarePackage时，子类型表示不同的软件包仓库，如BinObs、BinDevCloud（CodeArts软件发布库）。

        :param sub_type: The sub_type of this Source.
        :type sub_type: str
        """
        self._sub_type = sub_type

    @property
    def url(self):
        r"""Gets the url of this Source.

        url地址。 - 源类型为image时，url地址为镜像地址。 - 源类型为code时，url地址为git地址。 - 源类型为softwarePackage时，url地址为软件包地址。

        :return: The url of this Source.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Source.

        url地址。 - 源类型为image时，url地址为镜像地址。 - 源类型为code时，url地址为git地址。 - 源类型为softwarePackage时，url地址为软件包地址。

        :param url: The url of this Source.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, Source):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
