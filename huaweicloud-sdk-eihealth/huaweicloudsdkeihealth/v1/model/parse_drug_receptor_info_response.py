# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseDrugReceptorInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'residues': 'list[ResidueDto]',
        'ligands': 'list[ReceptorLigandInfoDto]'
    }

    attribute_map = {
        'residues': 'residues',
        'ligands': 'ligands'
    }

    def __init__(self, residues=None, ligands=None):
        """ParseDrugReceptorInfoResponse

        The model defined in huaweicloud sdk

        :param residues: 受体中的氨基酸残基列表
        :type residues: list[:class:`huaweicloudsdkeihealth.v1.ResidueDto`]
        :param ligands: 受体中的配体列表
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.ReceptorLigandInfoDto`]
        """
        
        super(ParseDrugReceptorInfoResponse, self).__init__()

        self._residues = None
        self._ligands = None
        self.discriminator = None

        if residues is not None:
            self.residues = residues
        if ligands is not None:
            self.ligands = ligands

    @property
    def residues(self):
        """Gets the residues of this ParseDrugReceptorInfoResponse.

        受体中的氨基酸残基列表

        :return: The residues of this ParseDrugReceptorInfoResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ResidueDto`]
        """
        return self._residues

    @residues.setter
    def residues(self, residues):
        """Sets the residues of this ParseDrugReceptorInfoResponse.

        受体中的氨基酸残基列表

        :param residues: The residues of this ParseDrugReceptorInfoResponse.
        :type residues: list[:class:`huaweicloudsdkeihealth.v1.ResidueDto`]
        """
        self._residues = residues

    @property
    def ligands(self):
        """Gets the ligands of this ParseDrugReceptorInfoResponse.

        受体中的配体列表

        :return: The ligands of this ParseDrugReceptorInfoResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ReceptorLigandInfoDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        """Sets the ligands of this ParseDrugReceptorInfoResponse.

        受体中的配体列表

        :param ligands: The ligands of this ParseDrugReceptorInfoResponse.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.ReceptorLigandInfoDto`]
        """
        self._ligands = ligands

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
        if not isinstance(other, ParseDrugReceptorInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
