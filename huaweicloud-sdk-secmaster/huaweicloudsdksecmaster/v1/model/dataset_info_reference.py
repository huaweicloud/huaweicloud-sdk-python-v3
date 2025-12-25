# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasetInfoReference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'csvc_display': 'str',
        'source_display': 'str',
        'link': 'str',
        'csvc_help': 'str',
        'source_help': 'str'
    }

    attribute_map = {
        'csvc_display': 'csvc_display',
        'source_display': 'source_display',
        'link': 'link',
        'csvc_help': 'csvc_help',
        'source_help': 'source_help'
    }

    def __init__(self, csvc_display=None, source_display=None, link=None, csvc_help=None, source_help=None):
        r"""DatasetInfoReference

        The model defined in huaweicloud sdk

        :param csvc_display: 云服务描述
        :type csvc_display: str
        :param source_display: 数据源描述
        :type source_display: str
        :param link: 链接
        :type link: str
        :param csvc_help: 云服务帮助说明
        :type csvc_help: str
        :param source_help: 数据源帮助说明
        :type source_help: str
        """
        
        

        self._csvc_display = None
        self._source_display = None
        self._link = None
        self._csvc_help = None
        self._source_help = None
        self.discriminator = None

        self.csvc_display = csvc_display
        self.source_display = source_display
        if link is not None:
            self.link = link
        if csvc_help is not None:
            self.csvc_help = csvc_help
        if source_help is not None:
            self.source_help = source_help

    @property
    def csvc_display(self):
        r"""Gets the csvc_display of this DatasetInfoReference.

        云服务描述

        :return: The csvc_display of this DatasetInfoReference.
        :rtype: str
        """
        return self._csvc_display

    @csvc_display.setter
    def csvc_display(self, csvc_display):
        r"""Sets the csvc_display of this DatasetInfoReference.

        云服务描述

        :param csvc_display: The csvc_display of this DatasetInfoReference.
        :type csvc_display: str
        """
        self._csvc_display = csvc_display

    @property
    def source_display(self):
        r"""Gets the source_display of this DatasetInfoReference.

        数据源描述

        :return: The source_display of this DatasetInfoReference.
        :rtype: str
        """
        return self._source_display

    @source_display.setter
    def source_display(self, source_display):
        r"""Sets the source_display of this DatasetInfoReference.

        数据源描述

        :param source_display: The source_display of this DatasetInfoReference.
        :type source_display: str
        """
        self._source_display = source_display

    @property
    def link(self):
        r"""Gets the link of this DatasetInfoReference.

        链接

        :return: The link of this DatasetInfoReference.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this DatasetInfoReference.

        链接

        :param link: The link of this DatasetInfoReference.
        :type link: str
        """
        self._link = link

    @property
    def csvc_help(self):
        r"""Gets the csvc_help of this DatasetInfoReference.

        云服务帮助说明

        :return: The csvc_help of this DatasetInfoReference.
        :rtype: str
        """
        return self._csvc_help

    @csvc_help.setter
    def csvc_help(self, csvc_help):
        r"""Sets the csvc_help of this DatasetInfoReference.

        云服务帮助说明

        :param csvc_help: The csvc_help of this DatasetInfoReference.
        :type csvc_help: str
        """
        self._csvc_help = csvc_help

    @property
    def source_help(self):
        r"""Gets the source_help of this DatasetInfoReference.

        数据源帮助说明

        :return: The source_help of this DatasetInfoReference.
        :rtype: str
        """
        return self._source_help

    @source_help.setter
    def source_help(self, source_help):
        r"""Sets the source_help of this DatasetInfoReference.

        数据源帮助说明

        :param source_help: The source_help of this DatasetInfoReference.
        :type source_help: str
        """
        self._source_help = source_help

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatasetInfoReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
