# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDETrashArtifactModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'format': 'str',
        'status': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'format': 'format',
        'status': 'status',
        'uri': 'uri'
    }

    def __init__(self, id=None, format=None, status=None, uri=None):
        r"""IDETrashArtifactModel

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 仓库id，格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页-&gt;仓库概览-&gt;仓库地址 url 中获取，最后两个\&quot;/\&quot;中间的字符串即为仓库id。 **约束限制**: 根据仓库id格式中region, domainId需要为有效值，format有效值为:npm|go|pypi|rpm|composer|maven|debian|conan|nuget|docker2|cocoapods|ohpm, sequence取值根据套餐不同有不同上限值。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type id: str
        :param format: **参数解释**: 制品类型。 **约束限制**: 不涉及。 **取值范围**: maven2|docker|npm|go|pypi|rpm|composer|debian|conan|nuget|docker2|cocoapods|ohpm|generic。 **默认取值**: 无。
        :type format: str
        :param status: **参数解释**: 当前仓库状态。 **约束限制**: 不涉及。 **取值范围**: active：正常。 trash：废弃。 delete：删除。 **默认取值**: 无。
        :type status: str
        :param uri: **参数解释**: 待还原的仓库路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type uri: str
        """
        
        

        self._id = None
        self._format = None
        self._status = None
        self._uri = None
        self.discriminator = None

        self.id = id
        self.format = format
        self.status = status
        self.uri = uri

    @property
    def id(self):
        r"""Gets the id of this IDETrashArtifactModel.

        **参数解释**: 仓库id，格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页->仓库概览->仓库地址 url 中获取，最后两个\"/\"中间的字符串即为仓库id。 **约束限制**: 根据仓库id格式中region, domainId需要为有效值，format有效值为:npm|go|pypi|rpm|composer|maven|debian|conan|nuget|docker2|cocoapods|ohpm, sequence取值根据套餐不同有不同上限值。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The id of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IDETrashArtifactModel.

        **参数解释**: 仓库id，格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页->仓库概览->仓库地址 url 中获取，最后两个\"/\"中间的字符串即为仓库id。 **约束限制**: 根据仓库id格式中region, domainId需要为有效值，format有效值为:npm|go|pypi|rpm|composer|maven|debian|conan|nuget|docker2|cocoapods|ohpm, sequence取值根据套餐不同有不同上限值。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param id: The id of this IDETrashArtifactModel.
        :type id: str
        """
        self._id = id

    @property
    def format(self):
        r"""Gets the format of this IDETrashArtifactModel.

        **参数解释**: 制品类型。 **约束限制**: 不涉及。 **取值范围**: maven2|docker|npm|go|pypi|rpm|composer|debian|conan|nuget|docker2|cocoapods|ohpm|generic。 **默认取值**: 无。

        :return: The format of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this IDETrashArtifactModel.

        **参数解释**: 制品类型。 **约束限制**: 不涉及。 **取值范围**: maven2|docker|npm|go|pypi|rpm|composer|debian|conan|nuget|docker2|cocoapods|ohpm|generic。 **默认取值**: 无。

        :param format: The format of this IDETrashArtifactModel.
        :type format: str
        """
        self._format = format

    @property
    def status(self):
        r"""Gets the status of this IDETrashArtifactModel.

        **参数解释**: 当前仓库状态。 **约束限制**: 不涉及。 **取值范围**: active：正常。 trash：废弃。 delete：删除。 **默认取值**: 无。

        :return: The status of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IDETrashArtifactModel.

        **参数解释**: 当前仓库状态。 **约束限制**: 不涉及。 **取值范围**: active：正常。 trash：废弃。 delete：删除。 **默认取值**: 无。

        :param status: The status of this IDETrashArtifactModel.
        :type status: str
        """
        self._status = status

    @property
    def uri(self):
        r"""Gets the uri of this IDETrashArtifactModel.

        **参数解释**: 待还原的仓库路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The uri of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this IDETrashArtifactModel.

        **参数解释**: 待还原的仓库路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param uri: The uri of this IDETrashArtifactModel.
        :type uri: str
        """
        self._uri = uri

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
        if not isinstance(other, IDETrashArtifactModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
