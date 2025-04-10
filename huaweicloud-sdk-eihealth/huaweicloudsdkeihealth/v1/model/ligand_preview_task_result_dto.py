# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LigandPreviewTaskResultDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'ligands': 'list[LigandPreviewInfoDto]',
        'has_more': 'bool'
    }

    attribute_map = {
        'count': 'count',
        'ligands': 'ligands',
        'has_more': 'has_more'
    }

    def __init__(self, count=None, ligands=None, has_more=None):
        r"""LigandPreviewTaskResultDto

        The model defined in huaweicloud sdk

        :param count: 已知的配体数量
        :type count: int
        :param ligands: 预览配体信息列表
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewInfoDto`]
        :param has_more: 文件中是否还有更多配体没有处理；即当前数量是否表示整个文件的配体数量，若该值为false则表该配体文件含有count数量个配体；若该值为true则表示改配体文件含有大于count数量个配体（即count不完全统计）；例如：count&#x3D;100且has_more&#x3D;true，则前端可显示该配体文件含有\&quot;100+个\&quot;小分子
        :type has_more: bool
        """
        
        

        self._count = None
        self._ligands = None
        self._has_more = None
        self.discriminator = None

        self.count = count
        self.ligands = ligands
        self.has_more = has_more

    @property
    def count(self):
        r"""Gets the count of this LigandPreviewTaskResultDto.

        已知的配体数量

        :return: The count of this LigandPreviewTaskResultDto.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this LigandPreviewTaskResultDto.

        已知的配体数量

        :param count: The count of this LigandPreviewTaskResultDto.
        :type count: int
        """
        self._count = count

    @property
    def ligands(self):
        r"""Gets the ligands of this LigandPreviewTaskResultDto.

        预览配体信息列表

        :return: The ligands of this LigandPreviewTaskResultDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewInfoDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        r"""Sets the ligands of this LigandPreviewTaskResultDto.

        预览配体信息列表

        :param ligands: The ligands of this LigandPreviewTaskResultDto.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewInfoDto`]
        """
        self._ligands = ligands

    @property
    def has_more(self):
        r"""Gets the has_more of this LigandPreviewTaskResultDto.

        文件中是否还有更多配体没有处理；即当前数量是否表示整个文件的配体数量，若该值为false则表该配体文件含有count数量个配体；若该值为true则表示改配体文件含有大于count数量个配体（即count不完全统计）；例如：count=100且has_more=true，则前端可显示该配体文件含有\"100+个\"小分子

        :return: The has_more of this LigandPreviewTaskResultDto.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this LigandPreviewTaskResultDto.

        文件中是否还有更多配体没有处理；即当前数量是否表示整个文件的配体数量，若该值为false则表该配体文件含有count数量个配体；若该值为true则表示改配体文件含有大于count数量个配体（即count不完全统计）；例如：count=100且has_more=true，则前端可显示该配体文件含有\"100+个\"小分子

        :param has_more: The has_more of this LigandPreviewTaskResultDto.
        :type has_more: bool
        """
        self._has_more = has_more

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
        if not isinstance(other, LigandPreviewTaskResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
