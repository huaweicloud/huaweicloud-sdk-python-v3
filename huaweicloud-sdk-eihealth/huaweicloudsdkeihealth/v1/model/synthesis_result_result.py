# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SynthesisResultResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'molecules': 'list[SynthesisResultResultMolecules]',
        'reactions': 'list[SynthesisResultResultReactions]',
        'synthesis_routes': 'list[SynthesisResultItem]'
    }

    attribute_map = {
        'molecules': 'molecules',
        'reactions': 'reactions',
        'synthesis_routes': 'synthesis_routes'
    }

    def __init__(self, molecules=None, reactions=None, synthesis_routes=None):
        """SynthesisResultResult

        The model defined in huaweicloud sdk

        :param molecules: 分子合成规划中的分子
        :type molecules: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultResultMolecules`]
        :param reactions: 分子合成规划中的反应列表
        :type reactions: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultResultReactions`]
        :param synthesis_routes: 分子合成规划的具体信息
        :type synthesis_routes: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultItem`]
        """
        
        

        self._molecules = None
        self._reactions = None
        self._synthesis_routes = None
        self.discriminator = None

        self.molecules = molecules
        self.reactions = reactions
        self.synthesis_routes = synthesis_routes

    @property
    def molecules(self):
        """Gets the molecules of this SynthesisResultResult.

        分子合成规划中的分子

        :return: The molecules of this SynthesisResultResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultResultMolecules`]
        """
        return self._molecules

    @molecules.setter
    def molecules(self, molecules):
        """Sets the molecules of this SynthesisResultResult.

        分子合成规划中的分子

        :param molecules: The molecules of this SynthesisResultResult.
        :type molecules: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultResultMolecules`]
        """
        self._molecules = molecules

    @property
    def reactions(self):
        """Gets the reactions of this SynthesisResultResult.

        分子合成规划中的反应列表

        :return: The reactions of this SynthesisResultResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultResultReactions`]
        """
        return self._reactions

    @reactions.setter
    def reactions(self, reactions):
        """Sets the reactions of this SynthesisResultResult.

        分子合成规划中的反应列表

        :param reactions: The reactions of this SynthesisResultResult.
        :type reactions: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultResultReactions`]
        """
        self._reactions = reactions

    @property
    def synthesis_routes(self):
        """Gets the synthesis_routes of this SynthesisResultResult.

        分子合成规划的具体信息

        :return: The synthesis_routes of this SynthesisResultResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultItem`]
        """
        return self._synthesis_routes

    @synthesis_routes.setter
    def synthesis_routes(self, synthesis_routes):
        """Sets the synthesis_routes of this SynthesisResultResult.

        分子合成规划的具体信息

        :param synthesis_routes: The synthesis_routes of this SynthesisResultResult.
        :type synthesis_routes: list[:class:`huaweicloudsdkeihealth.v1.SynthesisResultItem`]
        """
        self._synthesis_routes = synthesis_routes

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
        if not isinstance(other, SynthesisResultResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
