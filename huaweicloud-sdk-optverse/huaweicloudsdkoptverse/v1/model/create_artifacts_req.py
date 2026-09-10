# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateArtifactsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filenames': 'list[str]',
        'stage_name': 'StageName'
    }

    attribute_map = {
        'filenames': 'filenames',
        'stage_name': 'stage_name'
    }

    def __init__(self, filenames=None, stage_name=None):
        r"""CreateArtifactsReq

        The model defined in huaweicloud sdk

        :param filenames: **参数解释**： 标签列表。 **约束限制**： 产物列表不能超过10条。 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type filenames: list[str]
        :param stage_name: 
        :type stage_name: :class:`huaweicloudsdkoptverse.v1.StageName`
        """
        
        

        self._filenames = None
        self._stage_name = None
        self.discriminator = None

        self.filenames = filenames
        self.stage_name = stage_name

    @property
    def filenames(self):
        r"""Gets the filenames of this CreateArtifactsReq.

        **参数解释**： 标签列表。 **约束限制**： 产物列表不能超过10条。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The filenames of this CreateArtifactsReq.
        :rtype: list[str]
        """
        return self._filenames

    @filenames.setter
    def filenames(self, filenames):
        r"""Sets the filenames of this CreateArtifactsReq.

        **参数解释**： 标签列表。 **约束限制**： 产物列表不能超过10条。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param filenames: The filenames of this CreateArtifactsReq.
        :type filenames: list[str]
        """
        self._filenames = filenames

    @property
    def stage_name(self):
        r"""Gets the stage_name of this CreateArtifactsReq.

        :return: The stage_name of this CreateArtifactsReq.
        :rtype: :class:`huaweicloudsdkoptverse.v1.StageName`
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        r"""Sets the stage_name of this CreateArtifactsReq.

        :param stage_name: The stage_name of this CreateArtifactsReq.
        :type stage_name: :class:`huaweicloudsdkoptverse.v1.StageName`
        """
        self._stage_name = stage_name

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
        if not isinstance(other, CreateArtifactsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
