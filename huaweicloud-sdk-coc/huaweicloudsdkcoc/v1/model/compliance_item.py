# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComplianceItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'title': 'str',
        'classification': 'str',
        'severity_level': 'str',
        'compliance_level': 'str',
        'patch_detail': 'PatchDetail'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'title': 'title',
        'classification': 'classification',
        'severity_level': 'severity_level',
        'compliance_level': 'compliance_level',
        'patch_detail': 'patch_detail'
    }

    def __init__(self, instance_id=None, title=None, classification=None, severity_level=None, compliance_level=None, patch_detail=None):
        r"""ComplianceItem

        The model defined in huaweicloud sdk

        :param instance_id: 节点id
        :type instance_id: str
        :param title: 补丁名称
        :type title: str
        :param classification: 分类
        :type classification: str
        :param severity_level: 严重性级别
        :type severity_level: str
        :param compliance_level: 合规性级别
        :type compliance_level: str
        :param patch_detail: 
        :type patch_detail: :class:`huaweicloudsdkcoc.v1.PatchDetail`
        """
        
        

        self._instance_id = None
        self._title = None
        self._classification = None
        self._severity_level = None
        self._compliance_level = None
        self._patch_detail = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if title is not None:
            self.title = title
        if classification is not None:
            self.classification = classification
        if severity_level is not None:
            self.severity_level = severity_level
        if compliance_level is not None:
            self.compliance_level = compliance_level
        if patch_detail is not None:
            self.patch_detail = patch_detail

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ComplianceItem.

        节点id

        :return: The instance_id of this ComplianceItem.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ComplianceItem.

        节点id

        :param instance_id: The instance_id of this ComplianceItem.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def title(self):
        r"""Gets the title of this ComplianceItem.

        补丁名称

        :return: The title of this ComplianceItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ComplianceItem.

        补丁名称

        :param title: The title of this ComplianceItem.
        :type title: str
        """
        self._title = title

    @property
    def classification(self):
        r"""Gets the classification of this ComplianceItem.

        分类

        :return: The classification of this ComplianceItem.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        r"""Sets the classification of this ComplianceItem.

        分类

        :param classification: The classification of this ComplianceItem.
        :type classification: str
        """
        self._classification = classification

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ComplianceItem.

        严重性级别

        :return: The severity_level of this ComplianceItem.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ComplianceItem.

        严重性级别

        :param severity_level: The severity_level of this ComplianceItem.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def compliance_level(self):
        r"""Gets the compliance_level of this ComplianceItem.

        合规性级别

        :return: The compliance_level of this ComplianceItem.
        :rtype: str
        """
        return self._compliance_level

    @compliance_level.setter
    def compliance_level(self, compliance_level):
        r"""Sets the compliance_level of this ComplianceItem.

        合规性级别

        :param compliance_level: The compliance_level of this ComplianceItem.
        :type compliance_level: str
        """
        self._compliance_level = compliance_level

    @property
    def patch_detail(self):
        r"""Gets the patch_detail of this ComplianceItem.

        :return: The patch_detail of this ComplianceItem.
        :rtype: :class:`huaweicloudsdkcoc.v1.PatchDetail`
        """
        return self._patch_detail

    @patch_detail.setter
    def patch_detail(self, patch_detail):
        r"""Sets the patch_detail of this ComplianceItem.

        :param patch_detail: The patch_detail of this ComplianceItem.
        :type patch_detail: :class:`huaweicloudsdkcoc.v1.PatchDetail`
        """
        self._patch_detail = patch_detail

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
        if not isinstance(other, ComplianceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
