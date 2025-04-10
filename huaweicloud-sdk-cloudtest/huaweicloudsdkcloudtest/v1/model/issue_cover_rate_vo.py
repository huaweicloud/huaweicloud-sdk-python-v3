# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueCoverRateVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'epic': 'CoverRateVo',
        'feature': 'CoverRateVo',
        'story': 'CoverRateVo',
        'summary': 'CoverRateVo'
    }

    attribute_map = {
        'epic': 'epic',
        'feature': 'feature',
        'story': 'story',
        'summary': 'summary'
    }

    def __init__(self, epic=None, feature=None, story=None, summary=None):
        r"""IssueCoverRateVo

        The model defined in huaweicloud sdk

        :param epic: 
        :type epic: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        :param feature: 
        :type feature: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        :param story: 
        :type story: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        :param summary: 
        :type summary: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        
        

        self._epic = None
        self._feature = None
        self._story = None
        self._summary = None
        self.discriminator = None

        if epic is not None:
            self.epic = epic
        if feature is not None:
            self.feature = feature
        if story is not None:
            self.story = story
        if summary is not None:
            self.summary = summary

    @property
    def epic(self):
        r"""Gets the epic of this IssueCoverRateVo.

        :return: The epic of this IssueCoverRateVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        return self._epic

    @epic.setter
    def epic(self, epic):
        r"""Sets the epic of this IssueCoverRateVo.

        :param epic: The epic of this IssueCoverRateVo.
        :type epic: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        self._epic = epic

    @property
    def feature(self):
        r"""Gets the feature of this IssueCoverRateVo.

        :return: The feature of this IssueCoverRateVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this IssueCoverRateVo.

        :param feature: The feature of this IssueCoverRateVo.
        :type feature: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        self._feature = feature

    @property
    def story(self):
        r"""Gets the story of this IssueCoverRateVo.

        :return: The story of this IssueCoverRateVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        return self._story

    @story.setter
    def story(self, story):
        r"""Sets the story of this IssueCoverRateVo.

        :param story: The story of this IssueCoverRateVo.
        :type story: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        self._story = story

    @property
    def summary(self):
        r"""Gets the summary of this IssueCoverRateVo.

        :return: The summary of this IssueCoverRateVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this IssueCoverRateVo.

        :param summary: The summary of this IssueCoverRateVo.
        :type summary: :class:`huaweicloudsdkcloudtest.v1.CoverRateVo`
        """
        self._summary = summary

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
        if not isinstance(other, IssueCoverRateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
