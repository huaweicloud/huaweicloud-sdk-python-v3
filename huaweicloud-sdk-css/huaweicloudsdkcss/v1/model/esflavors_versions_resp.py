# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsflavorsVersionsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'flavors': 'list[EsflavorsVersionsFlavorsResp]',
        'type': 'str'
    }

    attribute_map = {
        'version': 'version',
        'flavors': 'flavors',
        'type': 'type'
    }

    def __init__(self, version=None, flavors=None, type=None):
        r"""EsflavorsVersionsResp

        The model defined in huaweicloud sdk

        :param version: Esasticsearch引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。
        :type version: str
        :param flavors: 规格列表。
        :type flavors: list[:class:`huaweicloudsdkcss.v1.EsflavorsVersionsFlavorsResp`]
        :param type: 实例类型，包括为ess、ess-cold、ess-master和ess-client。
        :type type: str
        """
        
        

        self._version = None
        self._flavors = None
        self._type = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if flavors is not None:
            self.flavors = flavors
        if type is not None:
            self.type = type

    @property
    def version(self):
        r"""Gets the version of this EsflavorsVersionsResp.

        Esasticsearch引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。

        :return: The version of this EsflavorsVersionsResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this EsflavorsVersionsResp.

        Esasticsearch引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。

        :param version: The version of this EsflavorsVersionsResp.
        :type version: str
        """
        self._version = version

    @property
    def flavors(self):
        r"""Gets the flavors of this EsflavorsVersionsResp.

        规格列表。

        :return: The flavors of this EsflavorsVersionsResp.
        :rtype: list[:class:`huaweicloudsdkcss.v1.EsflavorsVersionsFlavorsResp`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this EsflavorsVersionsResp.

        规格列表。

        :param flavors: The flavors of this EsflavorsVersionsResp.
        :type flavors: list[:class:`huaweicloudsdkcss.v1.EsflavorsVersionsFlavorsResp`]
        """
        self._flavors = flavors

    @property
    def type(self):
        r"""Gets the type of this EsflavorsVersionsResp.

        实例类型，包括为ess、ess-cold、ess-master和ess-client。

        :return: The type of this EsflavorsVersionsResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EsflavorsVersionsResp.

        实例类型，包括为ess、ess-cold、ess-master和ess-client。

        :param type: The type of this EsflavorsVersionsResp.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, EsflavorsVersionsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
