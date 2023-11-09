# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoundDeployVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploys': 'list[DeployVo]',
        'round_id': 'int'
    }

    attribute_map = {
        'deploys': 'deploys',
        'round_id': 'round_id'
    }

    def __init__(self, deploys=None, round_id=None):
        """RoundDeployVo

        The model defined in huaweicloud sdk

        :param deploys: deploy
        :type deploys: list[:class:`huaweicloudsdktics.v1.DeployVo`]
        :param round_id: 轮数
        :type round_id: int
        """
        
        

        self._deploys = None
        self._round_id = None
        self.discriminator = None

        if deploys is not None:
            self.deploys = deploys
        if round_id is not None:
            self.round_id = round_id

    @property
    def deploys(self):
        """Gets the deploys of this RoundDeployVo.

        deploy

        :return: The deploys of this RoundDeployVo.
        :rtype: list[:class:`huaweicloudsdktics.v1.DeployVo`]
        """
        return self._deploys

    @deploys.setter
    def deploys(self, deploys):
        """Sets the deploys of this RoundDeployVo.

        deploy

        :param deploys: The deploys of this RoundDeployVo.
        :type deploys: list[:class:`huaweicloudsdktics.v1.DeployVo`]
        """
        self._deploys = deploys

    @property
    def round_id(self):
        """Gets the round_id of this RoundDeployVo.

        轮数

        :return: The round_id of this RoundDeployVo.
        :rtype: int
        """
        return self._round_id

    @round_id.setter
    def round_id(self, round_id):
        """Sets the round_id of this RoundDeployVo.

        轮数

        :param round_id: The round_id of this RoundDeployVo.
        :type round_id: int
        """
        self._round_id = round_id

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
        if not isinstance(other, RoundDeployVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
