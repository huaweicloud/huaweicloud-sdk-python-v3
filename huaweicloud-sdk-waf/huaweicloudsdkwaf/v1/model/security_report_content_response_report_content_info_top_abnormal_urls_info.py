# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'abnormal_502_info_list': 'list[SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal502InfoList]',
        'abnormal_500_info_list': 'list[SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal500InfoList]',
        'abnormal_404_info_list': 'list[SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal404InfoList]'
    }

    attribute_map = {
        'abnormal_502_info_list': 'abnormal_502_info_list',
        'abnormal_500_info_list': 'abnormal_500_info_list',
        'abnormal_404_info_list': 'abnormal_404_info_list'
    }

    def __init__(self, abnormal_502_info_list=None, abnormal_500_info_list=None, abnormal_404_info_list=None):
        r"""SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo

        The model defined in huaweicloud sdk

        :param abnormal_502_info_list: **参数解释：** TOP返回502错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type abnormal_502_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal502InfoList`]
        :param abnormal_500_info_list: **参数解释：** TOP返回500错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type abnormal_500_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal500InfoList`]
        :param abnormal_404_info_list: **参数解释：** TOP返回404错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type abnormal_404_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal404InfoList`]
        """
        
        

        self._abnormal_502_info_list = None
        self._abnormal_500_info_list = None
        self._abnormal_404_info_list = None
        self.discriminator = None

        if abnormal_502_info_list is not None:
            self.abnormal_502_info_list = abnormal_502_info_list
        if abnormal_500_info_list is not None:
            self.abnormal_500_info_list = abnormal_500_info_list
        if abnormal_404_info_list is not None:
            self.abnormal_404_info_list = abnormal_404_info_list

    @property
    def abnormal_502_info_list(self):
        r"""Gets the abnormal_502_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.

        **参数解释：** TOP返回502错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The abnormal_502_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal502InfoList`]
        """
        return self._abnormal_502_info_list

    @abnormal_502_info_list.setter
    def abnormal_502_info_list(self, abnormal_502_info_list):
        r"""Sets the abnormal_502_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.

        **参数解释：** TOP返回502错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param abnormal_502_info_list: The abnormal_502_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.
        :type abnormal_502_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal502InfoList`]
        """
        self._abnormal_502_info_list = abnormal_502_info_list

    @property
    def abnormal_500_info_list(self):
        r"""Gets the abnormal_500_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.

        **参数解释：** TOP返回500错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The abnormal_500_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal500InfoList`]
        """
        return self._abnormal_500_info_list

    @abnormal_500_info_list.setter
    def abnormal_500_info_list(self, abnormal_500_info_list):
        r"""Sets the abnormal_500_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.

        **参数解释：** TOP返回500错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param abnormal_500_info_list: The abnormal_500_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.
        :type abnormal_500_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal500InfoList`]
        """
        self._abnormal_500_info_list = abnormal_500_info_list

    @property
    def abnormal_404_info_list(self):
        r"""Gets the abnormal_404_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.

        **参数解释：** TOP返回404错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The abnormal_404_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal404InfoList`]
        """
        return self._abnormal_404_info_list

    @abnormal_404_info_list.setter
    def abnormal_404_info_list(self, abnormal_404_info_list):
        r"""Sets the abnormal_404_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.

        **参数解释：** TOP返回404错误的URL列表，按错误次数排序。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param abnormal_404_info_list: The abnormal_404_info_list of this SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo.
        :type abnormal_404_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfoAbnormal404InfoList`]
        """
        self._abnormal_404_info_list = abnormal_404_info_list

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
