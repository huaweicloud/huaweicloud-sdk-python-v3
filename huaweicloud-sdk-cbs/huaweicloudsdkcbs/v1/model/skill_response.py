# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkillResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'skill_id': 'str',
        'skill_version': 'str',
        'frame': 'Frame',
        'candidate': 'CandidateIntention',
        'locked': 'bool',
        'related_intenions': 'list[RelatedIntention]'
    }

    attribute_map = {
        'skill_id': 'skill_id',
        'skill_version': 'skill_version',
        'frame': 'frame',
        'candidate': 'candidate',
        'locked': 'locked',
        'related_intenions': 'related_intenions'
    }

    def __init__(self, skill_id=None, skill_version=None, frame=None, candidate=None, locked=None, related_intenions=None):
        """SkillResponse

        The model defined in huaweicloud sdk

        :param skill_id: 技能ID。
        :type skill_id: str
        :param skill_version: 技能模型版本。
        :type skill_version: str
        :param frame: 
        :type frame: :class:`huaweicloudsdkcbs.v1.Frame`
        :param candidate: 
        :type candidate: :class:`huaweicloudsdkcbs.v1.CandidateIntention`
        :param locked: 技能是否锁定。
        :type locked: bool
        :param related_intenions: 相关意图信息。
        :type related_intenions: list[:class:`huaweicloudsdkcbs.v1.RelatedIntention`]
        """
        
        

        self._skill_id = None
        self._skill_version = None
        self._frame = None
        self._candidate = None
        self._locked = None
        self._related_intenions = None
        self.discriminator = None

        self.skill_id = skill_id
        self.skill_version = skill_version
        self.frame = frame
        self.candidate = candidate
        self.locked = locked
        self.related_intenions = related_intenions

    @property
    def skill_id(self):
        """Gets the skill_id of this SkillResponse.

        技能ID。

        :return: The skill_id of this SkillResponse.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """Sets the skill_id of this SkillResponse.

        技能ID。

        :param skill_id: The skill_id of this SkillResponse.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def skill_version(self):
        """Gets the skill_version of this SkillResponse.

        技能模型版本。

        :return: The skill_version of this SkillResponse.
        :rtype: str
        """
        return self._skill_version

    @skill_version.setter
    def skill_version(self, skill_version):
        """Sets the skill_version of this SkillResponse.

        技能模型版本。

        :param skill_version: The skill_version of this SkillResponse.
        :type skill_version: str
        """
        self._skill_version = skill_version

    @property
    def frame(self):
        """Gets the frame of this SkillResponse.

        :return: The frame of this SkillResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.Frame`
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this SkillResponse.

        :param frame: The frame of this SkillResponse.
        :type frame: :class:`huaweicloudsdkcbs.v1.Frame`
        """
        self._frame = frame

    @property
    def candidate(self):
        """Gets the candidate of this SkillResponse.

        :return: The candidate of this SkillResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.CandidateIntention`
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """Sets the candidate of this SkillResponse.

        :param candidate: The candidate of this SkillResponse.
        :type candidate: :class:`huaweicloudsdkcbs.v1.CandidateIntention`
        """
        self._candidate = candidate

    @property
    def locked(self):
        """Gets the locked of this SkillResponse.

        技能是否锁定。

        :return: The locked of this SkillResponse.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this SkillResponse.

        技能是否锁定。

        :param locked: The locked of this SkillResponse.
        :type locked: bool
        """
        self._locked = locked

    @property
    def related_intenions(self):
        """Gets the related_intenions of this SkillResponse.

        相关意图信息。

        :return: The related_intenions of this SkillResponse.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.RelatedIntention`]
        """
        return self._related_intenions

    @related_intenions.setter
    def related_intenions(self, related_intenions):
        """Sets the related_intenions of this SkillResponse.

        相关意图信息。

        :param related_intenions: The related_intenions of this SkillResponse.
        :type related_intenions: list[:class:`huaweicloudsdkcbs.v1.RelatedIntention`]
        """
        self._related_intenions = related_intenions

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
        if not isinstance(other, SkillResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
