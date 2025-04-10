# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCpiJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'DrugJobDto',
        'receptors': 'list[ReceptorDrugFile]',
        'ligands': 'list[MoleculeFileDto]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptors': 'receptors',
        'ligands': 'ligands'
    }

    def __init__(self, basic_info=None, receptors=None, ligands=None):
        r"""ShowCpiJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param receptors: 受体文件列表
        :type receptors: list[:class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`]
        :param ligands: 小分子
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`]
        """
        
        super(ShowCpiJobResponse, self).__init__()

        self._basic_info = None
        self._receptors = None
        self._ligands = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if receptors is not None:
            self.receptors = receptors
        if ligands is not None:
            self.ligands = ligands

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowCpiJobResponse.

        :return: The basic_info of this ShowCpiJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowCpiJobResponse.

        :param basic_info: The basic_info of this ShowCpiJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def receptors(self):
        r"""Gets the receptors of this ShowCpiJobResponse.

        受体文件列表

        :return: The receptors of this ShowCpiJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`]
        """
        return self._receptors

    @receptors.setter
    def receptors(self, receptors):
        r"""Sets the receptors of this ShowCpiJobResponse.

        受体文件列表

        :param receptors: The receptors of this ShowCpiJobResponse.
        :type receptors: list[:class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`]
        """
        self._receptors = receptors

    @property
    def ligands(self):
        r"""Gets the ligands of this ShowCpiJobResponse.

        小分子

        :return: The ligands of this ShowCpiJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        r"""Sets the ligands of this ShowCpiJobResponse.

        小分子

        :param ligands: The ligands of this ShowCpiJobResponse.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`]
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
        if not isinstance(other, ShowCpiJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
