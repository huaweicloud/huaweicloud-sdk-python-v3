# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTargetOptJobResponse(SdkResponse):

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
        'receptor': 'TargetOptReceptor',
        'ligand': 'TargetOptLigand',
        'md_params': 'MdParam'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptor': 'receptor',
        'ligand': 'ligand',
        'md_params': 'md_params'
    }

    def __init__(self, basic_info=None, receptor=None, ligand=None, md_params=None):
        r"""ShowTargetOptJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.TargetOptReceptor`
        :param ligand: 
        :type ligand: :class:`huaweicloudsdkeihealth.v1.TargetOptLigand`
        :param md_params: 
        :type md_params: :class:`huaweicloudsdkeihealth.v1.MdParam`
        """
        
        super(ShowTargetOptJobResponse, self).__init__()

        self._basic_info = None
        self._receptor = None
        self._ligand = None
        self._md_params = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if receptor is not None:
            self.receptor = receptor
        if ligand is not None:
            self.ligand = ligand
        if md_params is not None:
            self.md_params = md_params

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowTargetOptJobResponse.

        :return: The basic_info of this ShowTargetOptJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowTargetOptJobResponse.

        :param basic_info: The basic_info of this ShowTargetOptJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def receptor(self):
        r"""Gets the receptor of this ShowTargetOptJobResponse.

        :return: The receptor of this ShowTargetOptJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TargetOptReceptor`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this ShowTargetOptJobResponse.

        :param receptor: The receptor of this ShowTargetOptJobResponse.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.TargetOptReceptor`
        """
        self._receptor = receptor

    @property
    def ligand(self):
        r"""Gets the ligand of this ShowTargetOptJobResponse.

        :return: The ligand of this ShowTargetOptJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TargetOptLigand`
        """
        return self._ligand

    @ligand.setter
    def ligand(self, ligand):
        r"""Sets the ligand of this ShowTargetOptJobResponse.

        :param ligand: The ligand of this ShowTargetOptJobResponse.
        :type ligand: :class:`huaweicloudsdkeihealth.v1.TargetOptLigand`
        """
        self._ligand = ligand

    @property
    def md_params(self):
        r"""Gets the md_params of this ShowTargetOptJobResponse.

        :return: The md_params of this ShowTargetOptJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MdParam`
        """
        return self._md_params

    @md_params.setter
    def md_params(self, md_params):
        r"""Sets the md_params of this ShowTargetOptJobResponse.

        :param md_params: The md_params of this ShowTargetOptJobResponse.
        :type md_params: :class:`huaweicloudsdkeihealth.v1.MdParam`
        """
        self._md_params = md_params

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
        if not isinstance(other, ShowTargetOptJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
