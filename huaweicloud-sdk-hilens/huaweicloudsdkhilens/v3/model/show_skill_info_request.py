# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSkillInfoRequest:

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
        'status': 'int',
        'version': 'str'
    }

    attribute_map = {
        'skill_id': 'skill_id',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, skill_id=None, status=None, version=None):
        """ShowSkillInfoRequest

        The model defined in huaweicloud sdk

        :param skill_id: 技能ID
        :type skill_id: str
        :param status: 技能审核状态状态，1表示审核通过，2表示审核不通过，0表示待审核
        :type status: int
        :param version: 技能版本
        :type version: str
        """
        
        

        self._skill_id = None
        self._status = None
        self._version = None
        self.discriminator = None

        self.skill_id = skill_id
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version

    @property
    def skill_id(self):
        """Gets the skill_id of this ShowSkillInfoRequest.

        技能ID

        :return: The skill_id of this ShowSkillInfoRequest.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """Sets the skill_id of this ShowSkillInfoRequest.

        技能ID

        :param skill_id: The skill_id of this ShowSkillInfoRequest.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def status(self):
        """Gets the status of this ShowSkillInfoRequest.

        技能审核状态状态，1表示审核通过，2表示审核不通过，0表示待审核

        :return: The status of this ShowSkillInfoRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowSkillInfoRequest.

        技能审核状态状态，1表示审核通过，2表示审核不通过，0表示待审核

        :param status: The status of this ShowSkillInfoRequest.
        :type status: int
        """
        self._status = status

    @property
    def version(self):
        """Gets the version of this ShowSkillInfoRequest.

        技能版本

        :return: The version of this ShowSkillInfoRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowSkillInfoRequest.

        技能版本

        :param version: The version of this ShowSkillInfoRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowSkillInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
