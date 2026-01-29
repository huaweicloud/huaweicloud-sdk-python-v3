# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyReference:

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
        'csvc_hzzelp': 'str',
        'link': 'str',
        'source_display': 'str',
        'source_help': 'str'
    }

    attribute_map = {
        'csvc_display': 'csvc_display',
        'csvc_hzzelp': 'csvc_hzzelp',
        'link': 'link',
        'source_display': 'source_display',
        'source_help': 'source_help'
    }

    def __init__(self, csvc_display=None, csvc_hzzelp=None, link=None, source_display=None, source_help=None):
        r"""ListCollectConfigResponseBodyReference

        The model defined in huaweicloud sdk

        :param csvc_display: 云产品名称
        :type csvc_display: str
        :param csvc_hzzelp: 云产品描述
        :type csvc_hzzelp: str
        :param link: 链接
        :type link: str
        :param source_display: 日志名称
        :type source_display: str
        :param source_help: 日志描述
        :type source_help: str
        """
        
        

        self._csvc_display = None
        self._csvc_hzzelp = None
        self._link = None
        self._source_display = None
        self._source_help = None
        self.discriminator = None

        if csvc_display is not None:
            self.csvc_display = csvc_display
        if csvc_hzzelp is not None:
            self.csvc_hzzelp = csvc_hzzelp
        if link is not None:
            self.link = link
        if source_display is not None:
            self.source_display = source_display
        if source_help is not None:
            self.source_help = source_help

    @property
    def csvc_display(self):
        r"""Gets the csvc_display of this ListCollectConfigResponseBodyReference.

        云产品名称

        :return: The csvc_display of this ListCollectConfigResponseBodyReference.
        :rtype: str
        """
        return self._csvc_display

    @csvc_display.setter
    def csvc_display(self, csvc_display):
        r"""Sets the csvc_display of this ListCollectConfigResponseBodyReference.

        云产品名称

        :param csvc_display: The csvc_display of this ListCollectConfigResponseBodyReference.
        :type csvc_display: str
        """
        self._csvc_display = csvc_display

    @property
    def csvc_hzzelp(self):
        r"""Gets the csvc_hzzelp of this ListCollectConfigResponseBodyReference.

        云产品描述

        :return: The csvc_hzzelp of this ListCollectConfigResponseBodyReference.
        :rtype: str
        """
        return self._csvc_hzzelp

    @csvc_hzzelp.setter
    def csvc_hzzelp(self, csvc_hzzelp):
        r"""Sets the csvc_hzzelp of this ListCollectConfigResponseBodyReference.

        云产品描述

        :param csvc_hzzelp: The csvc_hzzelp of this ListCollectConfigResponseBodyReference.
        :type csvc_hzzelp: str
        """
        self._csvc_hzzelp = csvc_hzzelp

    @property
    def link(self):
        r"""Gets the link of this ListCollectConfigResponseBodyReference.

        链接

        :return: The link of this ListCollectConfigResponseBodyReference.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this ListCollectConfigResponseBodyReference.

        链接

        :param link: The link of this ListCollectConfigResponseBodyReference.
        :type link: str
        """
        self._link = link

    @property
    def source_display(self):
        r"""Gets the source_display of this ListCollectConfigResponseBodyReference.

        日志名称

        :return: The source_display of this ListCollectConfigResponseBodyReference.
        :rtype: str
        """
        return self._source_display

    @source_display.setter
    def source_display(self, source_display):
        r"""Sets the source_display of this ListCollectConfigResponseBodyReference.

        日志名称

        :param source_display: The source_display of this ListCollectConfigResponseBodyReference.
        :type source_display: str
        """
        self._source_display = source_display

    @property
    def source_help(self):
        r"""Gets the source_help of this ListCollectConfigResponseBodyReference.

        日志描述

        :return: The source_help of this ListCollectConfigResponseBodyReference.
        :rtype: str
        """
        return self._source_help

    @source_help.setter
    def source_help(self, source_help):
        r"""Sets the source_help of this ListCollectConfigResponseBodyReference.

        日志描述

        :param source_help: The source_help of this ListCollectConfigResponseBodyReference.
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
        if not isinstance(other, ListCollectConfigResponseBodyReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
