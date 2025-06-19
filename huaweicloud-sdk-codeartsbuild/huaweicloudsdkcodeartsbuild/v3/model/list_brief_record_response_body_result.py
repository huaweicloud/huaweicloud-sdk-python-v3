# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBriefRecordResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'brief_build_record_dtos': 'list[BriefRecordItems]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'brief_build_record_dtos': 'brief_build_record_dtos'
    }

    def __init__(self, project_id=None, brief_build_record_dtos=None):
        r"""ListBriefRecordResponseBodyResult

        The model defined in huaweicloud sdk

        :param project_id: 需要查询的项目ID
        :type project_id: str
        :param brief_build_record_dtos: 简要构建信息列表
        :type brief_build_record_dtos: list[:class:`huaweicloudsdkcodeartsbuild.v3.BriefRecordItems`]
        """
        
        

        self._project_id = None
        self._brief_build_record_dtos = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if brief_build_record_dtos is not None:
            self.brief_build_record_dtos = brief_build_record_dtos

    @property
    def project_id(self):
        r"""Gets the project_id of this ListBriefRecordResponseBodyResult.

        需要查询的项目ID

        :return: The project_id of this ListBriefRecordResponseBodyResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListBriefRecordResponseBodyResult.

        需要查询的项目ID

        :param project_id: The project_id of this ListBriefRecordResponseBodyResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def brief_build_record_dtos(self):
        r"""Gets the brief_build_record_dtos of this ListBriefRecordResponseBodyResult.

        简要构建信息列表

        :return: The brief_build_record_dtos of this ListBriefRecordResponseBodyResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.BriefRecordItems`]
        """
        return self._brief_build_record_dtos

    @brief_build_record_dtos.setter
    def brief_build_record_dtos(self, brief_build_record_dtos):
        r"""Sets the brief_build_record_dtos of this ListBriefRecordResponseBodyResult.

        简要构建信息列表

        :param brief_build_record_dtos: The brief_build_record_dtos of this ListBriefRecordResponseBodyResult.
        :type brief_build_record_dtos: list[:class:`huaweicloudsdkcodeartsbuild.v3.BriefRecordItems`]
        """
        self._brief_build_record_dtos = brief_build_record_dtos

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
        if not isinstance(other, ListBriefRecordResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
